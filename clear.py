import os
import fnmatch

for root, dirs, files in os.walk("."):
    for filename in fnmatch.filter(files, "piece_*"):
        filepath = os.path.join(root, filename)
        try:
            os.remove(filepath)
            print(f"Deleted: {filepath}")
        except Exception as e:
            print(f"Failed to delete {filepath}: {e}")
