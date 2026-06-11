# ============================================================
# File Name : history_manager.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# History Manager Module:
# - Stores request/response history
# - Tracks traffic logs
# - Supports search & filtering
# - Session-based history management
# ============================================================


from datetime import datetime


class HistoryManager:

    def __init__(self):
        self.history = []

    # ========================================================
    # ADD ENTRY
    # ========================================================
    def add_entry(self, request: dict, response: dict = None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "request": request,
            "response": response
        }

        self.history.append(entry)

    # ========================================================
    # GET ALL HISTORY
    # ========================================================
    def get_all(self):
        return self.history

    # ========================================================
    # SEARCH HISTORY
    # ========================================================
    def search(self, keyword: str):
        results = []

        for entry in self.history:
            req = str(entry.get("request", {})).lower()
            res = str(entry.get("response", {})).lower()

            if keyword.lower() in req or keyword.lower() in res:
                results.append(entry)

        return results

    # ========================================================
    # FILTER BY METHOD
    # ========================================================
    def filter_by_method(self, method: str):
        results = []

        for entry in self.history:
            request = entry.get("request", {})

            if request.get("method", "").upper() == method.upper():
                results.append(entry)

        return results

    # ========================================================
    # CLEAR HISTORY
    # ========================================================
    def clear(self):
        self.history = []

    # ========================================================
    # SHOW SUMMARY
    # ========================================================
    def summary(self):
        return {
            "total_requests": len(self.history),
            "first_entry": self.history[0]["timestamp"] if self.history else None,
            "last_entry": self.history[-1]["timestamp"] if self.history else None
        }

    # ========================================================
    # PRINT HISTORY (DEBUG VIEW)
    # ========================================================
    def print_history(self):
        print("\n========== HTTP HISTORY ==========")

        if not self.history:
            print("No history available.")
            return

        for i, entry in enumerate(self.history, 1):
            print(f"\n[{i}] Time: {entry['timestamp']}")
            print(f"Request : {entry['request']}")
            print(f"Response: {entry['response']}")

        print("\n==================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    history = HistoryManager()

    history.add_entry(
        request={"method": "GET", "url": "http://example.com"},
        response={"status_code": 200}
    )

    history.add_entry(
        request={"method": "POST", "url": "http://test.com/login"},
        response={"status_code": 403}
    )

    history.print_history()

    print("\nSummary:", history.summary())