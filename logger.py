import logging
import time
import os
from datetime import datetime, timedelta

class LaggedFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        # Subtract 1 day (86400 seconds) from the created timestamp
        lagged_time = datetime.fromtimestamp(record.created - 86400)
        if datefmt:
            return lagged_time.strftime(datefmt)
        else:
            return lagged_time.isoformat()

class Logger:
    def __init__(self, peer_id):
        self.peer_id = peer_id
        log_file_path = f"log_peer_{self.peer_id}.log"

        # Create log directory if needed
        os.makedirs(str(peer_id), exist_ok=True)

        self.logger = logging.getLogger(f"Peer_{peer_id}_Logger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(log_file_path, mode='w')
        formatter = LaggedFormatter(
            fmt='%(asctime)s - Peer %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
        self.start_time = time.time()

    def log(self, message):
        self.logger.info(f"[{self.get_elapsed_time()}] {message}")

    def log_connection(self, peer_id_connected_to):
        self.log(f"Peer {self.peer_id} makes a connection to Peer {peer_id_connected_to}.")

    def log_disconnect(self, peer_id_disconnected_from):
        self.log(f"Peer {self.peer_id} terminates the connection with Peer {peer_id_disconnected_from}.")

    def log_change_preferred_neighbors(self, preferred_neighbors):
        neighbors_str = ", ".join(map(str, preferred_neighbors))
        self.log(f"Peer {self.peer_id} has the preferred neighbors {neighbors_str}.")

    def log_change_optimistically_unchoked_neighbor(self, optimistically_unchoked_neighbor):
        self.log(f"Peer {self.peer_id} has the optimistically unchoked neighbor {optimistically_unchoked_neighbor}.")

    def log_unchoking(self, peer_id_unchoked):
        self.log(f"Peer {self.peer_id} unchokes peer {peer_id_unchoked}.")

    def log_choking(self, peer_id_choked):
        self.log(f"Peer {self.peer_id} chokes peer {peer_id_choked}.")

    def log_received_have(self, sender_peer_id, piece_index):
        self.log(f"Peer {self.peer_id} received the 'have' message from Peer {sender_peer_id} for the piece {piece_index}.")

    def log_received_piece(self, sender_peer_id, piece_index, num_pieces_received):
        self.log(f"Peer {self.peer_id} has downloaded the piece {piece_index} from Peer {sender_peer_id}. Now the number of pieces it has is {num_pieces_received}.")

    def log_requested_piece(self, receiver_peer_id, piece_index):
        self.log(f"Peer {self.peer_id} sent a 'request' message to Peer {receiver_peer_id} for the piece {piece_index}.")

    def log_sent_piece(self, receiver_peer_id, piece_index):
        self.log(f"Peer {self.peer_id} sent the piece {piece_index} to Peer {receiver_peer_id}.")

    def log_download_complete(self):
        self.log(f"Peer {self.peer_id} has downloaded the complete file.")

    def get_elapsed_time(self):
        return f"{int(time.time() - self.start_time):02d}s"


