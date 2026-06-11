# ============================================================
# File Name : report_generator.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Report Generator Module:
# - Generates HTML reports
# - Generates JSON reports
# - Generates text summaries
# - Formats vulnerability data professionally
# ============================================================


import json
from datetime import datetime


class ReportGenerator:

    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir

    # ========================================================
    # GENERATE HTML REPORT
    # ========================================================
    def generate_html_report(self, summary: dict, filename="report.html"):

        html_content = f"""
        <html>
        <head>
            <title>CyberSecuritySuite Report</title>
            <style>
                body {{ font-family: Arial; background: #0f172a; color: #fff; }}
                .box {{ padding: 15px; margin: 10px; background: #1e293b; border-radius: 10px; }}
                h1 {{ color: #38bdf8; }}
                h2 {{ color: #fbbf24; }}
            </style>
        </head>
        <body>

        <h1>CyberSecuritySuite - Security Report</h1>

        <div class="box">
            <h2>Summary</h2>
            <p>Total Vulnerabilities: {summary.get('total_vulnerabilities')}</p>
            <p>Risk Score: {summary.get('risk_score')}</p>
            <p>Risk Level: {summary.get('risk_level')}</p>
            <p>Generated At: {datetime.now().isoformat()}</p>
        </div>

        <div class="box">
            <h2>Details</h2>
        """

        for vtype, items in summary.get("by_type", {}).items():
            html_content += f"<h3>{vtype} ({len(items)})</h3><ul>"

            for item in items:
                html_content += f"<li>{item.get('issue','No detail')}</li>"

            html_content += "</ul>"

        html_content += """
        </div>

        </body>
        </html>
        """

        file_path = f"{self.output_dir}/{filename}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return file_path

    # ========================================================
    # GENERATE JSON REPORT
    # ========================================================
    def generate_json_report(self, summary: dict, filename="report.json"):

        file_path = f"{self.output_dir}/{filename}"

        report_data = {
            "generated_at": datetime.now().isoformat(),
            "summary": summary
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)

        return file_path

    # ========================================================
    # GENERATE TEXT REPORT
    # ========================================================
    def generate_text_report(self, summary: dict, filename="report.txt"):

        file_path = f"{self.output_dir}/{filename}"

        content = []
        content.append("CYBERSECURITY SUITE REPORT")
        content.append("=" * 40)
        content.append(f"Total Issues : {summary.get('total_vulnerabilities')}")
        content.append(f"Risk Score   : {summary.get('risk_score')}")
        content.append(f"Risk Level   : {summary.get('risk_level')}")
        content.append(f"Generated At : {datetime.now().isoformat()}")
        content.append("\nDETAILS:\n")

        for vtype, items in summary.get("by_type", {}).items():
            content.append(f"\n[{vtype}]")

            for item in items:
                content.append(f"- {item.get('issue','No detail')}")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

        return file_path

    # ========================================================
    # GENERATE ALL REPORTS
    # ========================================================
    def generate_all(self, summary: dict):

        return {
            "html": self.generate_html_report(summary),
            "json": self.generate_json_report(summary),
            "text": self.generate_text_report(summary)
        }


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    sample_summary = {
        "total_vulnerabilities": 4,
        "risk_score": 35,
        "risk_level": "HIGH",
        "by_type": {
            "SQL Injection": [{"issue": "SQL error detected"}],
            "XSS": [{"issue": "Reflected script found"}],
            "Security Header": [{"issue": "Missing CSP"}]
        }
    }

    generator = ReportGenerator()
    reports = generator.generate_all(sample_summary)

    print("\nReports Generated:")
    for k, v in reports.items():
        print(f"{k.upper()} -> {v}")