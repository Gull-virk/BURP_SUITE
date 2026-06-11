# ============================================================
# File Name : json_exporter.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# JSON Exporter Module:
# - Export reports to JSON
# - Save structured scan results
# - Load exported reports
# - Pretty formatted output
# ============================================================

import json
import os
from datetime import datetime


class JSONExporter:

    def __init__(self, export_dir="exports"):
        self.export_dir = export_dir

        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    # ========================================================
    # EXPORT DATA
    # ========================================================
    def export(self, filename: str, report_data: dict):

        try:
            if not filename.endswith(".json"):
                filename += ".json"

            file_path = os.path.join(self.export_dir, filename)

            payload = {
                "metadata": {
                    "generated_at": datetime.now().isoformat(),
                    "generator": "CyberSecuritySuite JSON Exporter",
                    "version": "1.0.0"
                },
                "report": report_data
            }

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(payload, file, indent=4, ensure_ascii=False)

            return {
                "status": "success",
                "file": file_path
            }

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }

    # ========================================================
    # LOAD REPORT
    # ========================================================
    def load(self, filename: str):

        try:
            file_path = os.path.join(self.export_dir, filename)

            if not os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": "File not found"
                }

            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }

    # ========================================================
    # LIST EXPORTS
    # ========================================================
    def list_exports(self):

        try:
            return [
                file
                for file in os.listdir(self.export_dir)
                if file.endswith(".json")
            ]

        except Exception:
            return []

    # ========================================================
    # DELETE EXPORT
    # ========================================================
    def delete(self, filename: str):

        try:
            file_path = os.path.join(self.export_dir, filename)

            if os.path.exists(file_path):
                os.remove(file_path)

                return {
                    "status": "success",
                    "message": f"{filename} deleted"
                }

            return {
                "status": "error",
                "message": "File not found"
            }

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }

    # ========================================================
    # REPORT SUMMARY
    # ========================================================
    def summary(self):

        exports = self.list_exports()

        return {
            "total_exports": len(exports),
            "files": exports
        }


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    exporter = JSONExporter()

    sample_report = {
        "target": "https://example.com",
        "scan_type": "Passive",
        "findings": [
            {
                "name": "Missing Security Headers",
                "severity": "Medium"
            }
        ]
    }

    result = exporter.export(
        "sample_security_report",
        sample_report
    )

    print(result)

    print(exporter.summary())