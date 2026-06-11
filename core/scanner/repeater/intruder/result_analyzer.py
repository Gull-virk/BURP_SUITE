# ============================================================
# File Name : result_analyzer.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Result Analyzer Module:
# - Analyzes scan/attack results
# - Calculates risk score
# - Groups vulnerabilities
# - Generates final security insights
# ============================================================


class ResultAnalyzer:

    def __init__(self):
        self.results = []
        self.risk_score = 0

    # ========================================================
    # LOAD RESULTS
    # ========================================================
    def load_results(self, results: list):
        self.results.extend(results)

    # ========================================================
    # ANALYZE RESULTS
    # ========================================================
    def analyze(self):

        self.risk_score = 0

        for r in self.results:

            vuln = r.get("vulnerability")

            if vuln == "SQL Injection Suspected":
                self.risk_score += 10

            elif vuln == "XSS Suspected":
                self.risk_score += 8

            elif vuln == "Path Traversal Suspected":
                self.risk_score += 9

            elif r.get("type") == "Request Error":
                self.risk_score += 2

        return self.generate_summary()

    # ========================================================
    # GROUP RESULTS BY VULNERABILITY TYPE
    # ========================================================
    def group_by_vulnerability(self):
        grouped = {}

        for r in self.results:
            key = r.get("vulnerability") or r.get("type") or "Unknown"

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(r)

        return grouped

    # ========================================================
    # RISK LEVEL CALCULATION
    # ========================================================
    def risk_level(self):

        if self.risk_score >= 50:
            return "CRITICAL"
        elif self.risk_score >= 30:
            return "HIGH"
        elif self.risk_score >= 15:
            return "MEDIUM"
        else:
            return "LOW"

    # ========================================================
    # SUMMARY REPORT
    # ========================================================
    def generate_summary(self):

        summary = {
            "total_results": len(self.results),
            "risk_score": self.risk_score,
            "risk_level": self.risk_level(),
            "grouped_results": self.group_by_vulnerability()
        }

        return summary

    # ========================================================
    # PRINT REPORT
    # ========================================================
    def report(self):

        summary = self.generate_summary()

        print("\n========== RESULT ANALYSIS REPORT ==========")
        print(f"Total Results : {summary['total_results']}")
        print(f"Risk Score    : {summary['risk_score']}")
        print(f"Risk Level    : {summary['risk_level']}")

        print("\n--- Vulnerability Breakdown ---")

        for vtype, items in summary["grouped_results"].items():
            print(f"\n[{vtype}] ({len(items)})")

            for item in items:
                if "payload" in item:
                    print(f"  - Payload: {item.get('payload')} | URL: {item.get('url')}")
                else:
                    print(f"  - {item}")

        print("\n============================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    sample_results = [
        {"vulnerability": "SQL Injection Suspected", "payload": "' OR 1=1", "url": "http://test.com"},
        {"vulnerability": "XSS Suspected", "payload": "<script>", "url": "http://test.com"},
        {"vulnerability": "Path Traversal Suspected", "payload": "../../etc/passwd", "url": "http://test.com"},
        {"type": "Request Error", "payload": "test"}
    ]

    analyzer = ResultAnalyzer()
    analyzer.load_results(sample_results)

    analyzer.report()