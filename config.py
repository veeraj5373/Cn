import os

class Config:
    def __init__(self, common_config_path, peer_info_config_path):
        try:
            self.common_config = self.parse_common_config(common_config_path)
            self.peer_info = self.parse_peer_info(peer_info_config_path)
        except Exception as e:
            print(f"Error initializing Config: {e}")

    def parse_common_config(self, common_config_path):
        if not os.path.isfile(common_config_path):
            raise FileNotFoundError(f"Common config file '{common_config_path}' not found.")

        common_config = {}
        with open(common_config_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split(maxsplit=1)
                    common_config[key] = value
        return common_config

    def parse_peer_info(self, peer_info_config_path):
        peer_info = {}
        if not os.path.isfile(peer_info_config_path):
            raise FileNotFoundError(f"Peer information config file '{peer_info_config_path}' not found.")

        with open(peer_info_config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) == 4:
                        peer_id = int(parts[0])
                        hostname = parts[1]
                        port = int(parts[2])
                        has_file = int(parts[3])
                        peer_info[peer_id] = {'hostname': hostname, 'port': port, 'has_file': has_file}
                    else:
                        raise ValueError(f"Invalid peer info line format: '{line}'. Expected 4 parts.")
        return peer_info

    def get_common_config(self):
        return self.common_config

    def get_peer_info(self, peer_id):
        return self.peer_info.get(peer_id, None)

    def get_initial_peer_list(self, current_peer_id):
        return [(p_id, details['hostname'], details['port']) for p_id, details in self.peer_info.items() if p_id != current_peer_id]

    def has_complete_file(self, peer_id):
        return self.peer_info.get(peer_id, {}).get('has_file', 0) == 1


