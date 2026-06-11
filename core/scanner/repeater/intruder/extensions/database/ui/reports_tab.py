# ============================================================
# File Name : reports_tab.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Reports Tab Module:
# - Displays generated security reports
# - Loads saved reports
# - Summarizes vulnerabilities
# - UI-style report controller
# ============================================================


import os
import json
from datetime import datetime


class ReportsTab:

    def __init__(self, reports_dir="storage"):
        self.reports_dir = reports_dir
        self.reports = []

        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)

    # ========================================================
    # LOAD ALL REPORTS
    # ========================================================
    def load_reports(self):

        self.reports = []

        for file in os.listdir(self.reports_dir):

            if file.endswith(".json"):

                try:
                    path = os.path.join(self.reports_dir, file)

                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    self.reports.append({
                        "file": file,
                        "data": data
                    })

                except Exception as e:
                    print(f"[ERROR LOADING] {file} -> {str(e)}")

        return self.reports

    # ========================================================
    # GET REPORT BY FILE NAME
    # ========================================================
    def get_report(self, filename: str):

        path = os.path.join(self.reports_dir, filename)

        if not os.path.exists(path):
            return {"error": "Report not found"}

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # ========================================================
    # SUMMARY OF ALL REPORTS
    # ========================================================
    def summary(self):

        total = len(self.reports)
        total_vulns = 0
        high_risk = 0

        for r in self.reports:

            data = r.get("data", {}).get("summary", {})

            total_vulns += data.get("total_vulnerabilities", 0)

            if data.get("risk_level") == "HIGH" or data.get("risk_level") == "CRITICAL":
                high_risk += 1

        return {
            "total_reports": total,
            "total_vulnerabilities": total_vulns,
            "high_risk_reports": high_risk
        }

    # ========================================================
    # DELETE REPORT
    # ========================================================
    def delete_report(self, filename: str):

        path = os.path.join(self.reports_dir, filename)

        if os.path.exists(path):
            os.remove(path)
            return {"status": "deleted", "file": filename}

        return {"error": "File not found"}

    # ========================================================
    # SHOW REPORTS
    # ========================================================
    def show(self):

        print("\n========== REPORTS DASHBOARD ==========")

        if not self.reports:
            print("No reports available.")
            return

        for i, r in enumerate(self.reports, 1):

            data = r.get("data", {}).get("summary", {})

            print(f"\n[{i}] File   : {r['file']}")
            print(f"    Vulns  : {data.get('total_vulnerabilities', 0)}")
            print(f"    Risk   : {data.get('risk_level', 'UNKNOWN')}")

        print("\n=======================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    tab = ReportsTab()

    tab.load_reports()

    tab.show()

    print("Summary:", tab.summary())