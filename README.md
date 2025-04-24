# CN-project

A fully functional Peer-to-Peer (P2P) file sharing network built using Python sockets, supporting both TCP and UDP protocols. Developed as part of a Computer Networks academic project to showcase the core principles of decentralized communication and file transfer.

---

## Overview

This project simulates a P2P network where each node (peer) can upload and download files without needing a centralized server. It models real-world P2P applications like BitTorrent in a simplified academic format.

---

## Features

- Peer discovery and communication  
- File segmentation and transfer  
- Custom protocol for message exchange  
- Logging and error handling  
- TCP-based reliable data transfer  
- UDP-based messaging (for control/signaling)  

---

## Project Structure

```
CN-project/
│
├── Common.cfg             # Global config: intervals, number of peers, file name
├── PeerInfo.cfg           # Individual peer info: ID, IP, port, file status
├── config.py              # Reads and parses configuration files
├── peer.py                # Main peer logic (server + client)
├── file_manager.py        # File splitting, joining, checking
├── message.py             # Defines message types and byte structure
├── logger.py              # Event logger
├── main.py                # Program entry point
├── requirements.sh        # Shell script to install Python requirements
├── PROJECT OUTLINE.pdf    # Project documentation (includes design + flow)
└── README.md              # You’re reading it!
```

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Linux/macOS (tested)
- Terminal access

### Clone the Repository

```bash
git clone https://github.com/veeraj5373/CN-project.git
cd CN-project
```

### Install Requirements

```bash
bash requirements.sh
```

---

## Configuration

### `Common.cfg`

Defines global constants used across all peers:

- NumberOfPreferredNeighbors
- UnchokingInterval
- OptimisticUnchokingInterval
- FileName
- FileSize
- PieceSize

### `PeerInfo.cfg`

Contains peer-specific information:

```
<PeerID> <Address> <Port> <HasFile>
```

Example:
```
1001 localhost 6008 1
1002 localhost 6009 0
```

---

## Running the Application

Open a separate terminal for each peer listed in `PeerInfo.cfg` and run:

```bash
python3 main.py <PeerID>
```

Where `<PeerID>` matches the one in your config file.

---

## Logging

Each peer creates its own log file:

```
log_peer_<PeerID>.log
```

This records:

- Connection events
- File request/receive
- Unchoke/choke notifications

---

## Project Goals

- Understand the mechanics of peer-to-peer networks  
- Practice socket programming using TCP/UDP  
- Explore concurrency with multithreading  
- Simulate real-world protocols in a controlled academic setup  

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

This project was developed as a university Computer Networks assignment. The architecture and logic closely follow academic P2P specifications with custom implementations.
