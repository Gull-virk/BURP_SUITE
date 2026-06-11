# ============================================================
# File Name : vulnerability_analyzer.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Vulnerability Analyzer Module:
# - Aggregates scan results
# - Calculates risk score
# - Categorizes vulnerabilities
# - Generates structured security report
# ============================================================


class VulnerabilityAnalyzer:

    def __init__(self):
        self.vulnerabilities = []
        self.risk_score = 0

    # ========================================================
    # LOAD FINDINGS
    # ========================================================
    def load_findings(self, findings: list):
        self.vulnerabilities.extend(findings)

    # ========================================================
    # ANALYZE ALL VULNERABILITIES
    # ========================================================
    def analyze(self):

        for vuln in self.vulnerabilities:
            severity = vuln.get("severity", "Low")

            if severity == "High":
                self.risk_score += 10
            elif severity == "Medium":
                self.risk_score += 5
            elif severity == "Low":
                self.risk_score += 2

        return self.generate_summary()

    # ========================================================
    # GROUP BY TYPE
    # ========================================================
    def group_by_type(self):
        grouped = {}

        for vuln in self.vulnerabilities:
            vtype = vuln.get("type", "Unknown")

            if vtype not in grouped:
                grouped[vtype] = []

            grouped[vtype].append(vuln)

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
            "total_vulnerabilities": len(self.vulnerabilities),
            "risk_score": self.risk_score,
            "risk_level": self.risk_level(),
            "by_type": self.group_by_type()
        }

        return summary

    # ========================================================
    # PRINT REPORT
    # ========================================================
    def report(self):

        summary = self.generate_summary()

        print("\n========== VULNERABILITY ANALYSIS REPORT ==========")
        print(f"Total Issues   : {summary['total_vulnerabilities']}")
        print(f"Risk Score     : {summary['risk_score']}")
        print(f"Risk Level     : {summary['risk_level']}")

        print("\n--- Breakdown by Type ---")
        for vtype, items in summary["by_type"].items():
            print(f"\n{vtype} ({len(items)})")
            for item in items:
                print(f"  - {item.get('issue', 'No details')}")

        print("\n===================================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    sample_findings = [
        {"type": "SQL Injection", "severity": "High", "issue": "SQL error detected"},
        {"type": "XSS", "severity": "High", "issue": "Reflected script found"},
        {"type": "Security Header", "severity": "Medium", "issue": "Missing CSP header"},
        {"type": "Cookie Security", "severity": "Low", "issue": "Missing Secure flag"}
    ]

    analyzer = VulnerabilityAnalyzer()
    analyzer.load_findings(sample_findings)

    analyzer.report()