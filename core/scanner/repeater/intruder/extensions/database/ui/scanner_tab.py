# ============================================================
# File Name : scanner_tab.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Scanner Tab Module:
# - Handles scan input (target URL)
# - Starts active/passive scanning
# - Integrates with attack engine
# - Displays scan status
# ============================================================


from datetime import datetime


class ScannerTab:

    def __init__(self):
        self.target_url = None
        self.scan_status = "IDLE"
        self.results = []

    # ========================================================
    # SET TARGET
    # ========================================================
    def set_target(self, url: str):
        self.target_url = url
        print(f"[TARGET SET] {url}")

    # ========================================================
    # START SCAN (SIMULATION ENTRY POINT)
    # ========================================================
    def start_scan(self):
        if not self.target_url:
            return "No target set"

        self.scan_status = "RUNNING"
        print(f"[SCAN STARTED] {self.target_url}")

        # Simulated scan process
        self.results = [
            {
                "type": "Passive Check",
                "status": "OK",
                "time": datetime.now().isoformat()
            },
            {
                "type": "Header Analysis",
                "status": "Missing Security Headers",
                "time": datetime.now().isoformat()
            }
        ]

        self.scan_status = "COMPLETED"
        return self.results

    # ========================================================
    # GET STATUS
    # ========================================================
    def get_status(self):
        return {
            "target": self.target_url,
            "status": self.scan_status,
            "results_count": len(self.results)
        }

    # ========================================================
    # SHOW RESULTS
    # ========================================================
    def show_results(self):
        print("\n========== SCAN RESULTS ==========")

        if not self.results:
            print("No results available.")
            return

        for i, r in enumerate(self.results, 1):
            print(f"\n[{i}] Type  : {r['type']}")
            print(f"    Status: {r['status']}")
            print(f"    Time  : {r['time']}")

        print("\n==================================\n")

    # ========================================================
    # RESET SCAN
    # ========================================================
    def reset(self):
        self.target_url = None
        self.scan_status = "IDLE"
        self.results = []


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    scanner = ScannerTab()

    scanner.set_target("http://example.com")

    scanner.start_scan()

    scanner.show_results()

    print(scanner.get_status())