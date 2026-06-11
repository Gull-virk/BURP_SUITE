# ============================================================
# File Name : passive_scanner.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Passive Security Scanner:
# - Analyzes HTTP responses
# - Detects missing security headers
# - Finds basic security misconfigurations
# - Non-intrusive scanning (no attacks)
# ============================================================


class PassiveScanner:

    def __init__(self):
        self.findings = []

    # ========================================================
    # MAIN SCAN FUNCTION
    # ========================================================
    def scan(self, response_data: dict):
        self.findings = []

        self.check_security_headers(response_data)
        self.check_information_disclosure(response_data)
        self.check_cookies(response_data)

        return self.findings

    # ========================================================
    # CHECK SECURITY HEADERS
    # ========================================================
    def check_security_headers(self, response_data):
        headers = response_data.get("headers", {})

        security_headers = {
            "Content-Security-Policy": "Missing CSP header",
            "X-Frame-Options": "Missing X-Frame-Options (Clickjacking risk)",
            "X-XSS-Protection": "Missing XSS Protection header",
            "Strict-Transport-Security": "Missing HSTS header"
        }

        for header, issue in security_headers.items():
            if header not in headers:
                self.findings.append({
                    "type": "Security Header",
                    "severity": "Medium",
                    "issue": issue,
                    "header": header
                })

    # ========================================================
    # CHECK INFORMATION DISCLOSURE
    # ========================================================
    def check_information_disclosure(self, response_data):
        body = response_data.get("body", "").lower()

        sensitive_keywords = [
            "sql syntax",
            "stack trace",
            "exception",
            "warning",
            "fatal error",
            "debug",
            "traceback"
        ]

        for keyword in sensitive_keywords:
            if keyword in body:
                self.findings.append({
                    "type": "Information Disclosure",
                    "severity": "Low",
                    "issue": f"Possible sensitive info: {keyword}"
                })

    # ========================================================
    # CHECK COOKIE SECURITY
    # ========================================================
    def check_cookies(self, response_data):
        headers = response_data.get("headers", {})

        cookies = headers.get("Set-Cookie", "")

        if cookies:
            if "HttpOnly" not in cookies:
                self.findings.append({
                    "type": "Cookie Security",
                    "severity": "Medium",
                    "issue": "Missing HttpOnly flag"
                })

            if "Secure" not in cookies:
                self.findings.append({
                    "type": "Cookie Security",
                    "severity": "Medium",
                    "issue": "Missing Secure flag"
                })

            if "SameSite" not in cookies:
                self.findings.append({
                    "type": "Cookie Security",
                    "severity": "Low",
                    "issue": "Missing SameSite attribute"
                })

    # ========================================================
    # GET RESULTS
    # ========================================================
    def get_findings(self):
        return self.findings

    # ========================================================
    # PRINT REPORT
    # ========================================================
    def report(self):
        print("\n========== PASSIVE SCAN REPORT ==========")

        if not self.findings:
            print("No issues found.")
            return

        for i, finding in enumerate(self.findings, 1):
            print(f"\n[{i}] Type    : {finding['type']}")
            print(f"    Severity: {finding['severity']}")
            print(f"    Issue   : {finding['issue']}")

        print("\n========================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    sample_response = {
        "headers": {
            "Content-Type": "text/html"
        },
        "body": "<html><h1>SQL syntax error</h1></html>"
    }

    scanner = PassiveScanner()
    results = scanner.scan(sample_response)

    scanner.report()