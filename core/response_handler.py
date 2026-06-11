# ============================================================
# File Name : response_handler.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Handles HTTP responses:
# - Parses raw response
# - Extracts status code, headers, body
# - Formats response for analysis
# - Supports logging & debugging
# ============================================================

from datetime import datetime


class ResponseHandler:

    # ========================================================
    # PARSE RAW HTTP RESPONSE
    # ========================================================
    def parse_response(self, raw_response: str):
        try:
            lines = raw_response.split("\n")

            # First line: HTTP/1.1 200 OK
            status_line = lines[0].split(" ", 2)

            protocol = status_line[0]
            status_code = status_line[1] if len(status_line) > 1 else "000"
            status_message = status_line[2] if len(status_line) > 2 else ""

            headers = {}
            body = ""

            is_body = False

            for line in lines[1:]:
                if line.strip() == "":
                    is_body = True
                    continue

                if not is_body:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        headers[parts[0].strip()] = parts[1].strip()
                else:
                    body += line + "\n"

            response_data = {
                "protocol": protocol,
                "status_code": status_code,
                "status_message": status_message,
                "headers": headers,
                "body": body.strip(),
                "timestamp": datetime.now().isoformat()
            }

            return response_data

        except Exception as e:
            return {
                "error": str(e),
                "raw_response": raw_response
            }

    # ========================================================
    # CHECK RESPONSE STATUS
    # ========================================================
    def is_success(self, response_data: dict):
        try:
            return str(response_data.get("status_code")) in ["200", "201", "202", "204"]
        except:
            return False

    # ========================================================
    # SIMPLE RESPONSE ANALYZER
    # ========================================================
    def analyze_response(self, response_data: dict):
        analysis = {
            "status_code": response_data.get("status_code"),
            "length": len(response_data.get("body", "")),
            "has_cookie": "set-cookie" in str(response_data.get("headers", {})).lower(),
            "content_type": response_data.get("headers", {}).get("Content-Type", "unknown"),
            "security_headers": {
                "x-frame-options": "X-Frame-Options" in response_data.get("headers", {}),
                "x-xss-protection": "X-XSS-Protection" in response_data.get("headers", {}),
                "content_security_policy": "Content-Security-Policy" in response_data.get("headers", {})
            },
            "timestamp": datetime.now().isoformat()
        }

        return analysis

    # ========================================================
    # LOG RESPONSE
    # ========================================================
    def log_response(self, response_data: dict):
        print("\n========== RESPONSE LOG ==========")
        print(f"Status Code : {response_data.get('status_code')}")
        print(f"Message      : {response_data.get('status_message')}")
        print(f"Body Length  : {len(response_data.get('body', ''))}")
        print(f"Time         : {response_data.get('timestamp')}")
        print("=================================\n")