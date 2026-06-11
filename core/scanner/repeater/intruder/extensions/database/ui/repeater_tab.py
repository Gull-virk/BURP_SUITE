# ============================================================
# File Name : repeater_tab.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Repeater Tab Module:
# - Re-send HTTP requests multiple times
# - Modify request before sending
# - Compare responses
# - Debug & testing tool
# ============================================================


import requests
from datetime import datetime


class RepeaterTab:

    def __init__(self):
        self.history = []

    # ========================================================
    # SEND REQUEST
    # ========================================================
    def send(self, method: str, url: str, headers=None, body=None):

        try:
            headers = headers or {}

            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                data=body,
                timeout=10
            )

            result = {
                "request": {
                    "method": method,
                    "url": url,
                    "headers": headers,
                    "body": body
                },
                "response": {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "body": response.text
                },
                "time": datetime.now().isoformat()
            }

            self.history.append(result)

            return result

        except Exception as e:
            return {
                "error": str(e),
                "time": datetime.now().isoformat()
            }

    # ========================================================
    # RESEND LAST REQUEST
    # ========================================================
    def resend_last(self):
        if not self.history:
            return {"error": "No request history"}

        last = self.history[-1]["request"]
        return self.send(
            last["method"],
            last["url"],
            last.get("headers"),
            last.get("body")
        )

    # ========================================================
    # GET HISTORY
    # ========================================================
    def get_history(self):
        return self.history

    # ========================================================
    # CLEAR HISTORY
    # ========================================================
    def clear(self):
        self.history = []

    # ========================================================
    # PRINT RESPONSE SUMMARY
    # ========================================================
    def show_history(self):
        print("\n========== REPEATER HISTORY ==========")

        if not self.history:
            print("No requests found.")
            return

        for i, item in enumerate(self.history, 1):
            req = item["request"]
            res = item["response"]

            print(f"\n[{i}] {req['method']} {req['url']}")
            print(f"    Status: {res['status_code']}")
            print(f"    Time  : {item['time']}")

        print("\n======================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    repeater = RepeaterTab()

    result = repeater.send(
        "GET",
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print(result["response"]["status_code"])

    repeater.show_history()

    repeater.resend_last()