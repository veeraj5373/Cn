import sys
from peer import Peer

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <peer_id>")
        sys.exit(1)

    try:
        peer_id = int(sys.argv[1])
        peer = Peer(peer_id)

        # Keep the main thread alive so other threads continue running
        while True:
            pass

    except ValueError:
        print("Error: Peer ID must be an integer.")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"Peer {peer_id} shutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)