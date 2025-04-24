import struct

class Message:
    CHOKE = 0
    UNCHOKE = 1
    INTERESTED = 2
    NOT_INTERESTED = 3
    HAVE = 4
    BITFIELD = 5
    REQUEST = 6
    PIECE = 7
    COMPLETE = 8


    @staticmethod
    def choke():
        return struct.pack(">IB", 1, Message.CHOKE)

    @staticmethod
    def unchoke():
        return struct.pack(">IB", 1, Message.UNCHOKE)

    @staticmethod
    def interested():
        return struct.pack(">IB", 1, Message.INTERESTED)

    @staticmethod
    def not_interested():
        return struct.pack(">IB", 1, Message.NOT_INTERESTED)

    @staticmethod
    def have(piece_index):
        payload = struct.pack(">I", piece_index)
        return struct.pack(">IB", 1 + len(payload), Message.HAVE) + payload

    @staticmethod
    def bitfield(bitfield_data):
        return struct.pack(">IB", 1 + len(bitfield_data), Message.BITFIELD) + bitfield_data

    @staticmethod
    def request(piece_index):
        payload = struct.pack(">I", piece_index)
        return struct.pack(">IB", 1 + len(payload), Message.REQUEST) + payload

    @staticmethod
    def piece(piece_index, data):
        payload = struct.pack(">I", piece_index) + data
        return struct.pack(">IB", 1 + len(payload), Message.PIECE) + payload
    
    @staticmethod
    def interested():
        return struct.pack('>IB', 1, 2)  # Length = 1, ID = 2

    @staticmethod
    def not_interested():
        return struct.pack('>IB', 1, 3)  # Length = 1, ID = 3

    @staticmethod
    def complete():
        return struct.pack(">IB", 1, 8)
    
    @staticmethod
    def completion_update(peer_ids):
        """Send peer IDs as newline-separated string"""
        payload = "\n".join(str(pid) for pid in peer_ids).encode('utf-8')
        return struct.pack(">IB", 1 + len(payload), 9) + payload  # ID 9 for completion update

    @staticmethod
    def global_complete():
        return struct.pack(">IB", 1, 10)

    
    @staticmethod
    def parse_message(data):
        if len(data) < 5:
            return None, None

        length = struct.unpack(">I", data[:4])[0]
        message_id = struct.unpack(">B", data[4:5])[0]
        payload = data[5:5 + (length - 1)]

        return message_id, payload
