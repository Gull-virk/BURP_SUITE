# ============================================================
# File Name : text_proxy.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Text Proxy Module
# - Receives text input
# - Applies filters
# - Logs processing activity
# - Returns processed text
# ============================================================

from datetime import datetime


class TextProxy:

    def __init__(self):
        self.history = []

    # ========================================================
    # PROCESS TEXT
    # ========================================================
    def process(self, text: str) -> str:

        result = text.strip()

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "original_length": len(text),
            "processed_length": len(result)
        }

        self.history.append(log_entry)

        return result

    # ========================================================
    # CONVERT TO UPPERCASE
    # ========================================================
    def to_upper(self, text: str) -> str:
        return text.upper()

    # ========================================================
    # CONVERT TO LOWERCASE
    # ========================================================
    def to_lower(self, text: str) -> str:
        return text.lower()

    # ========================================================
    # REMOVE EXTRA SPACES
    # ========================================================
    def normalize_spaces(self, text: str) -> str:
        return " ".join(text.split())

    # ========================================================
    # GET HISTORY
    # ========================================================
    def get_history(self):
        return self.history

    # ========================================================
    # CLEAR HISTORY
    # ========================================================
    def clear_history(self):
        self.history.clear()

    # ========================================================
    # SHOW STATS
    # ========================================================
    def stats(self):
        return {
            "processed_items": len(self.history)
        }


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    proxy = TextProxy()

    sample = "   Hello   CyberSecuritySuite   "

    cleaned = proxy.process(sample)

    print("Processed :", cleaned)
    print("Upper     :", proxy.to_upper(cleaned))
    print("Lower     :", proxy.to_lower(cleaned))
    print("History   :", proxy.get_history())