# ============================================================
# File Name : api_manager.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# API Manager Module:
# - Handles API requests
# - Manages endpoints
# - Standardizes responses
# - Supports security tool integrations
# ============================================================


import requests
import json


class APIManager:

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.base_headers = {
            "Content-Type": "application/json",
            "User-Agent": "CyberSecuritySuite-API/1.0"
        }
        self.endpoints = {}

    # ========================================================
    # REGISTER ENDPOINT
    # ========================================================
    def register_endpoint(self, name: str, url: str, method: str = "GET"):
        self.endpoints[name] = {
            "url": url,
            "method": method.upper()
        }

    # ========================================================
    # CALL API
    # ========================================================
    def call(self, name: str, data: dict = None, params: dict = None):

        if name not in self.endpoints:
            return {"error": "Endpoint not found"}

        endpoint = self.endpoints[name]

        try:
            method = endpoint["method"]
            url = endpoint["url"]

            if method == "GET":
                response = requests.get(
                    url,
                    headers=self.base_headers,
                    params=params,
                    timeout=self.timeout
                )

            elif method == "POST":
                response = requests.post(
                    url,
                    headers=self.base_headers,
                    json=data,
                    timeout=self.timeout
                )

            elif method == "PUT":
                response = requests.put(
                    url,
                    headers=self.base_headers,
                    json=data,
                    timeout=self.timeout
                )

            elif method == "DELETE":
                response = requests.delete(
                    url,
                    headers=self.base_headers,
                    timeout=self.timeout
                )

            else:
                return {"error": "Unsupported HTTP method"}

            return self._format_response(response)

        except Exception as e:
            return {"error": str(e)}

    # ========================================================
    # FORMAT RESPONSE
    # ========================================================
    def _format_response(self, response):
        try:
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": response.text,
                "json": response.json() if "application/json" in response.headers.get("Content-Type", "") else None
            }
        except Exception as e:
            return {"error": str(e)}

    # ========================================================
    # LIST ENDPOINTS
    # ========================================================
    def list_endpoints(self):
        return self.endpoints

    # ========================================================
    # TEST CONNECTION
    # ========================================================
    def test(self, url: str):
        try:
            response = requests.get(url, headers=self.base_headers, timeout=self.timeout)
            return {"status_code": response.status_code}
        except Exception as e:
            return {"error": str(e)}


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    api = APIManager()

    api.register_endpoint("example", "https://jsonplaceholder.typicode.com/posts/1", "GET")

    result = api.call("example")

    print(json.dumps(result, indent=4))