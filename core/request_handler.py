# ============================================================
# File Name : request_handler.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Handles incoming HTTP/HTTPS requests:
# - Parses raw requests
# - Extracts method, URL, headers, body
# - Normalizes request structure
# - Prepares for proxy/scanner modules
# ============================================================

from urllib.parse import urlparse
from datetime import datetime


class RequestHandler:

    # ========================================================
    # PARSE RAW HTTP REQUEST
    # ========================================================
    def parse_request(self, raw_request: str):
        try:
            lines = raw_request.split("\n")

            # First line: METHOD URL HTTP/1.1
            request_line = lines[0].split()

            method = request_line[0]
            url = request_line[1]
            protocol = request_line[2] if len(request_line) > 2 else "HTTP/1.1"

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

            parsed_url = urlparse(url)

            request_data = {
                "method": method,
                "url": url,
                "protocol": protocol,
                "host": parsed_url.hostname,
                "path": parsed_url.path,
                "query": parsed_url.query,
                "headers": headers,
                "body": body.strip(),
                "timestamp": datetime.now().isoformat()
            }

            return request_data

        except Exception as e:
            return {
                "error": str(e),
                "raw_request": raw_request
            }

    # ========================================================
    # FORMAT REQUEST BACK TO RAW
    # ========================================================
    def build_request(self, request_data: dict):
        try:
            request_line = f"{request_data['method']} {request_data['path']} HTTP/1.1"

            headers = ""
            for key, value in request_data.get("headers", {}).items():
                headers += f"{key}: {value}\n"

            body = request_data.get("body", "")

            raw_request = f"{request_line}\n{headers}\n{body}"

            return raw_request

        except Exception as e:
            return f"Error building request: {str(e)}"

    # ========================================================
    # SIMPLE REQUEST LOGGING
    # ========================================================
    def log_request(self, request_data: dict):
        print("\n========== REQUEST LOG ==========")
        print(f"Method   : {request_data.get('method')}")
        print(f"URL      : {request_data.get('url')}")
        print(f"Host     : {request_data.get('host')}")
        print(f"Path     : {request_data.get('path')}")
        print(f"Time     : {request_data.get('timestamp')}")
        print("=================================\n")-