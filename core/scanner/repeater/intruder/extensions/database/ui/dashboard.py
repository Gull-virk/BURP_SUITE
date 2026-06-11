# ============================================================
# File Name : dashboard.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Dashboard Module:
# - System overview panel
# - Scanner status display
# - Quick actions menu
# - Real-time stats summary
# ============================================================


from datetime import datetime


class Dashboard:

    def __init__(self, version="1.0.0"):
        self.version = version
        self.modules = {
            "scanner": "ACTIVE",
            "history": "ACTIVE",
            "cache": "ACTIVE",
            "storage": "ACTIVE",
            "api": "ACTIVE"
        }

        self.stats = {
            "requests": 0,
            "vulnerabilities": 0,
            "sessions": 0
        }

    # ========================================================
    # UPDATE STATS
    # ========================================================
    def update_stats(self, requests=0, vulnerabilities=0, sessions=0):
        self.stats["requests"] += requests
        self.stats["vulnerabilities"] += vulnerabilities
        self.stats["sessions"] += sessions

    # ========================================================
    # SET MODULE STATUS
    # ========================================================
    def set_module_status(self, module: str, status: str):
        self.modules[module] = status.upper()

    # ========================================================
    # SHOW HEADER
    # ========================================================
    def header(self):
        print("\n" + "=" * 60)
        print("     CYBERSECURITY SUITE - CONTROL DASHBOARD")
        print("=" * 60)
        print(f"Version : {self.version}")
        print(f"Time    : {datetime.now().isoformat()}")
        print("=" * 60)

    # ========================================================
    # SHOW MODULE STATUS
    # ========================================================
    def show_modules(self):
        print("\n--- MODULE STATUS ---")

        for module, status in self.modules.items():
            print(f"{module.upper():15} : {status}")

    # ========================================================
    # SHOW STATS
    # ========================================================
    def show_stats(self):
        print("\n--- SYSTEM STATS ---")
        print(f"Total Requests      : {self.stats['requests']}")
        print(f"Vulnerabilities     : {self.stats['vulnerabilities']}")
        print(f"Active Sessions     : {self.stats['sessions']}")

    # ========================================================
    # QUICK ACTIONS
    # ========================================================
    def actions(self):
        print("\n--- QUICK ACTIONS ---")
        print("[1] Start Scan")
        print("[2] View History")
        print("[3] Run Attack Engine")
        print("[4] Generate Report")
        print("[5] Exit")

    # ========================================================
    # FULL DASHBOARD VIEW
    # ========================================================
    def show(self):
        self.header()
        self.show_modules()
        self.show_stats()
        self.actions()

    # ========================================================
    # SIMULATE ACTION
    # ========================================================
    def run_action(self, choice: int):
        if choice == 1:
            return "Starting Scanner..."
        elif choice == 2:
            return "Opening History..."
        elif choice == 3:
            return "Launching Attack Engine..."
        elif choice == 4:
            return "Generating Report..."
        elif choice == 5:
            return "Exiting System..."
        else:
            return "Invalid Option"


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    dashboard = Dashboard()

    dashboard.update_stats(requests=25, vulnerabilities=3, sessions=1)

    dashboard.show()

    print("\nAction Result:", dashboard.run_action(1))