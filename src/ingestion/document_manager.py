import os
import json
from pathlib import Path


class DocumentManager:
    @staticmethod
    def needs_processing(raw_dir="data/raw_documents",
                         processed_dir="data/processed",
                         metadata_file="processing_metadata.json"):
        """
        Returns True if:
        1. Any raw file has been modified since last processing
        2. New files have been added to raw_dir
        3. No processed files exist
        """
        metadata_path = Path(processed_dir) / metadata_file

        # First run: no metadata exists
        if not metadata_path.exists():
            return True

        # Load previous metadata
        with open(metadata_path, "r") as f:
            previous_state = json.load(f)

        # Scan current raw files
        current_state = {}
        for file_path in Path(raw_dir).iterdir():
            if file_path.is_file():
                stats = file_path.stat()
                current_state[file_path.name] = {
                    "mtime": stats.st_mtime_ns,  # Nanosecond precision
                    "size": stats.st_size
                }

        # Check for new/modified files
        for filename, curr_info in current_state.items():
            prev_info = previous_state.get(filename)

            # New file detected
            if not prev_info:
                return True

            # Modified file detected
            if (curr_info["mtime"] != prev_info["mtime"]) or \
                    (curr_info["size"] != prev_info["size"]):
                return True

        # Check for deleted files (optional)
        for filename in previous_state:
            if filename not in current_state:
                return True

        return False

    @staticmethod
    def save_processing_state(raw_dir, processed_dir, metadata_file="processing_metadata.json"):
        """
        Save current state of raw files for future comparisons
        """
        metadata = {}
        for file_path in Path(raw_dir).iterdir():
            if file_path.is_file():
                stats = file_path.stat()
                metadata[file_path.name] = {
                    "mtime": stats.st_mtime_ns,
                    "size": stats.st_size
                }

        metadata_path = Path(processed_dir) / metadata_file
        metadata_path.parent.mkdir(parents=True, exist_ok=True)

        with open(metadata_path, "w") as f:
            json.dump(metadata, f)


