import os

class FileManager:
    def __init__(self, file_name, file_size, piece_size, peer_id):
        self.file_name = file_name
        self.file_size = file_size
        self.piece_size = piece_size
        self.peer_id = peer_id
        self.source_dir = str(peer_id)  # Where the full file resides initially
        self.storage_dir = str(peer_id)  # Also use the same for saving pieces and final output
        os.makedirs(self.storage_dir, exist_ok=True)

    def calculate_piece_offset(self, piece_index):
        return piece_index * self.piece_size

    def calculate_piece_length(self, piece_index):
        offset = self.calculate_piece_offset(piece_index)
        remaining_bytes = self.file_size - offset
        return min(self.piece_size, remaining_bytes)

    def retrieve_piece(self, piece_index):
        file_path = os.path.join(self.storage_dir, f"piece_{piece_index}")
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None
        except IOError as e:
            print(f"Error reading piece {piece_index}: {e}")
            return None

    def save_piece(self, piece_index, data):
        file_path = os.path.join(self.storage_dir, f"piece_{piece_index}")
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
            return True
        except IOError as e:
            print(f"Error saving piece {piece_index}: {e}")
            return False

    def is_piece_avalible(self, piece_index):
        file_path = os.path.join(self.storage_dir, f"piece_{piece_index}")
        return os.path.exists(file_path)

    def has_complete_file(self):
        file_path = os.path.join(self.storage_dir, self.file_name)
        return os.path.exists(file_path) and os.path.getsize(file_path) == self.file_size

    def assemble_file(self, total_pieces):
        final_file_path = os.path.join(self.storage_dir, self.file_name)
        try:
            with open(final_file_path, 'wb') as outfile:
                for i in range(total_pieces):
                    piece_path = os.path.join(self.storage_dir, f"piece_{i}")
                    try:
                        with open(piece_path, 'rb') as infile:
                            outfile.write(infile.read())
                    except FileNotFoundError:
                        print(f"Missing piece {i}, cannot assemble complete file.")
                        return False
            return True
        except IOError as e:
            print(f"Error assembling file: {e}")
            return False

    def split_file_into_pieces(self):
        source_file_path = os.path.join(self.source_dir, self.file_name)
        try:
            with open(source_file_path, 'rb') as infile:
                for i in range((self.file_size + self.piece_size - 1) // self.piece_size):
                    offset = i * self.piece_size
                    bytes_to_read = self.calculate_piece_length(i)
                    infile.seek(offset)
                    data = infile.read(bytes_to_read)
                    self.save_piece(i, data)
            return True
        except FileNotFoundError:
            print(f"File not found: {source_file_path}")
            return False
        except IOError as e:
            print(f"Error reading source file: {e}")
            return False
