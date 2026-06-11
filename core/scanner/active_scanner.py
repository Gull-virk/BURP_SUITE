# ============================================================
# File Name : active_scanner.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Active Security Scanner:
# - Sends test requests (controlled)
# - Detects basic vulnerabilities
# - Compares responses
# - Used for authorized penetration testing only
# ============================================================

import requests
from urllib.parse import urljoin


class ActiveScanner:

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.findings = []

        self.payloads = [
            "'",
            "\"",
            "<script>alert(1)</script>",
            "../../etc/passwd",
            "admin'--"
        ]

        self.headers = {
            "User-Agent": "CyberSecuritySuite-ActiveScanner/1.0 (Educational Use Only)"
        }

    # ========================================================
    # MAIN SCAN FUNCTION
    # ========================================================
    def scan(self, base_url):
        self.findings = []

        print(f"[+] Starting Active Scan on: {base_url}")

        for payload in self.payloads:
            self.test_payload(base_url, payload)

        return self.findings

    # ========================================================
    # TEST PAYLOAD AGAINST TARGET
    # ========================================================
    def test_payload(self, url, payload):

        test_url = urljoin(url, f"?input={payload}")

        try:
            response = requests.get(
                test_url,
                headers=self.headers,
                timeout=self.timeout
            )

            self.analyze_response(test_url, response, payload)

        except Exception as e:
            self.findings.append({
                "type": "Request Error",
                "payload": payload,
                "error": str(e)
            })

    # ========================================================
    # RESPONSE ANALYSIS
    # ========================================================
    def analyze_response(self, url, response, payload):

        content = response.text.lower()

        # SQL error detection
        sql_errors = [
            "sql syntax",
            "mysql",
            "odbc",
            "warning: mysql",
            "unclosed quotation"
        ]

        # XSS reflection check
        reflected = payload.lower() in content

        for error in sql_errors:
            if error in content:
                self.findings.append({
                    "type": "SQL Injection Suspected",
                    "severity": "High",
                    "url": url,
                    "payload": payload,
                    "evidence": error
                })

        if reflected and "<script" in payload.lower():
            self.findings.append({
                "type": "XSS Suspected",
                "severity": "High",
                "url": url,
                "payload": payload,
                "evidence": "Payload reflected in response"
            })

        # Directory traversal hint
        if "root:" in content or "etc/passwd" in content:
            self.findings.append({
                "type": "Path Traversal Suspected",
                "severity": "High",
                "url": url,
                "payload": payload,
                "evidence": "Sensitive file pattern detected"
            })

    # ========================================================
    # GET RESULTS
    # ========================================================
    def get_findings(self):
        return self.findings

    # ========================================================
    # REPORT PRINT
    # ========================================================
    def report(self):
        print("\n========== ACTIVE SCAN REPORT ==========")

        if not self.findings:
            print("No vulnerabilities detected.")
            return

        for i, f in enumerate(self.findings, 1):
            print(f"\n[{i}] Type    : {f.get('type')}")
            print(f"    Severity: {f.get('severity', 'Low')}")
            print(f"    URL     : {f.get('url', '-')}")
            print(f"    Payload : {f.get('payload', '-')}")
            print(f"    Evidence: {f.get('evidence', '-')}")

        print("\n========================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    target = "http://example.com/search"

    scanner = ActiveScanner()
    results = scanner.scan(target)

    scanner.report()