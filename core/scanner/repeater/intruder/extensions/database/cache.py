# ============================================================
# File Name : cache.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Cache Module:
# - Stores temporary data in memory
# - Improves performance
# - TTL-based cache support
# - Used for scan optimization
# ============================================================


import time


class CacheManager:

    def __init__(self, ttl=300):
        """
        ttl = time to live (seconds)
        """
        self.ttl = ttl
        self.cache = {}

    # ========================================================
    # SET CACHE VALUE
    # ========================================================
    def set(self, key: str, value):
        self.cache[key] = {
            "value": value,
            "time": time.time()
        }

    # ========================================================
    # GET CACHE VALUE
    # ========================================================
    def get(self, key: str):
        if key not in self.cache:
            return None

        data = self.cache[key]

        # check expiration
        if time.time() - data["time"] > self.ttl:
            del self.cache[key]
            return None

        return data["value"]

    # ========================================================
    # CHECK KEY EXISTS
    # ========================================================
    def exists(self, key: str) -> bool:
        return self.get(key) is not None

    # ========================================================
    # DELETE CACHE KEY
    # ========================================================
    def delete(self, key: str):
        if key in self.cache:
            del self.cache[key]

    # ========================================================
    # CLEAR ALL CACHE
    # ========================================================
    def clear(self):
        self.cache = {}

    # ========================================================
    # CLEAN EXPIRED CACHE
    # ========================================================
    def cleanup(self):
        current_time = time.time()

        keys_to_delete = []

        for key, data in self.cache.items():
            if current_time - data["time"] > self.ttl:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self.cache[key]

    # ========================================================
    # CACHE SIZE
    # ========================================================
    def size(self):
        return len(self.cache)

    # ========================================================
    # DEBUG PRINT CACHE
    # ========================================================
    def debug(self):
        print("\n========== CACHE DUMP ==========")

        for key, data in self.cache.items():
            age = time.time() - data["time"]
            print(f"{key} -> age: {int(age)}s")

        print("=================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    cache = CacheManager(ttl=10)

    cache.set("user", {"name": "Gull", "role": "admin"})
    cache.set("token", "abc123")

    print(cache.get("user"))
    print("Exists token:", cache.exists("token"))

    cache.debug()