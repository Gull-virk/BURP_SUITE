# ============================================================
# File Name : storage.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Storage Module:
# - Saves data locally (JSON)
# - Loads stored data
# - Manages scan history persistence
# - Lightweight database layer
# ============================================================


import json
import os
from datetime import datetime


class StorageManager:

    def __init__(self, storage_dir="storage"):
        self.storage_dir = storage_dir

        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    # ========================================================
    # SAVE DATA TO FILE
    # ========================================================
    def save(self, filename: str, data: dict):
        try:
            file_path = os.path.join(self.storage_dir, filename)

            payload = {
                "saved_at": datetime.now().isoformat(),
                "data": data
            }

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=4)

            return {"status": "success", "file": file_path}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    # ========================================================
    # LOAD DATA FROM FILE
    # ========================================================
    def load(self, filename: str):
        try:
            file_path = os.path.join(self.storage_dir, filename)

            if not os.path.exists(file_path):
                return {"status": "error", "message": "File not found"}

            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception as e:
            return {"status": "error", "message": str(e)}

    # ========================================================
    # LIST ALL FILES
    # ========================================================
    def list_files(self):
        return os.listdir(self.storage_dir)

    # ========================================================
    # DELETE FILE
    # ========================================================
    def delete(self, filename: str):
        try:
            file_path = os.path.join(self.storage_dir, filename)

            if os.path.exists(file_path):
                os.remove(file_path)
                return {"status": "deleted", "file": filename}

            return {"status": "error", "message": "File not found"}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    # ========================================================
    # CLEAR ALL STORAGE
    # ========================================================
    def clear_all(self):
        try:
            for file in os.listdir(self.storage_dir):
                os.remove(os.path.join(self.storage_dir, file))

            return {"status": "cleared"}

        except Exception as e:
            return {"status": "error", "message": str(e)}


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    storage = StorageManager()

    sample_data = {
        "scan": "test",
        "result": "success"
    }

    save_result = storage.save("test.json", sample_data)
    print(save_result)

    loaded = storage.load("test.json")
    print(loaded)

    print("Files:", storage.list_files())