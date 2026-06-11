# ============================================================
# File Name : response_viewer.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Response Viewer Module:
# - Displays HTTP responses
# - Formats headers and body
# - Highlights status codes
# - Debug-friendly output
# ============================================================


from datetime import datetime
import json


class ResponseViewer:

    def __init__(self):
        self.response = {}

    # ========================================================
    # LOAD RESPONSE
    # ========================================================
    def load_response(self, response_data: dict):
        self.response = response_data

    # ========================================================
    # FORMAT HEADERS
    # ========================================================
    def format_headers(self):
        headers = self.response.get("headers", {})
        return "\n".join([f"{k}: {v}" for k, v in headers.items()])

    # ========================================================
    # GET STATUS INFO
    # ========================================================
    def get_status(self):
        return {
            "status_code": self.response.get("status_code", "N/A"),
            "status_message": self.response.get("status_message", "N/A"),
            "timestamp": self.response.get("timestamp", datetime.now().isoformat())
        }

    # ========================================================
    # VIEW BODY
    # ========================================================
    def get_body(self):
        body = self.response.get("body", "")

        # Try pretty JSON formatting
        try:
            return json.dumps(json.loads(body), indent=4)
        except:
            return body

    # ========================================================
    # FULL RESPONSE VIEW
    # ========================================================
    def view(self):
        print("\n========== RESPONSE VIEWER ==========")

        status = self.get_status()

        print(f"Status Code   : {status['status_code']}")
        print(f"Status Message: {status['status_message']}")
        print(f"Time          : {status['timestamp']}")

        print("\n--- Headers ---")
        print(self.format_headers() or "No headers")

        print("\n--- Body ---")
        print(self.get_body() or "Empty body")

        print("\n=====================================\n")

    # ========================================================
    # EXPORT RESPONSE
    # ========================================================
    def export(self, filename="response.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.response, f, indent=4)

            return filename

        except Exception as e:
            return f"Export error: {str(e)}"


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    sample_response = {
        "status_code": 200,
        "status_message": "OK",
        "headers": {
            "Content-Type": "application/json",
            "Server": "CyberSuite"
        },
        "body": '{"message": "Hello World"}',
        "timestamp": datetime.now().isoformat()
    }

    viewer = ResponseViewer()
    viewer.load_response(sample_response)

    viewer.view()

    file = viewer.export()
    print(f"Response exported to: {file}")