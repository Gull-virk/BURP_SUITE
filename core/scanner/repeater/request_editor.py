# ============================================================
# File Name : request_editor.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Request Editor Module:
# - Modify HTTP requests
# - Edit headers, parameters, body
# - Rebuild raw request
# - Used for testing & debugging only
# ============================================================


class RequestEditor:

    def __init__(self):
        self.request_data = {}

    # ========================================================
    # LOAD REQUEST
    # ========================================================
    def load_request(self, request_data: dict):
        self.request_data = request_data

    # ========================================================
    # EDIT METHOD
    # ========================================================
    def set_method(self, method: str):
        self.request_data["method"] = method.upper()

    # ========================================================
    # EDIT URL
    # ========================================================
    def set_url(self, url: str):
        self.request_data["url"] = url

    # ========================================================
    # EDIT HEADERS
    # ========================================================
    def set_header(self, key: str, value: str):
        if "headers" not in self.request_data:
            self.request_data["headers"] = {}

        self.request_data["headers"][key] = value

    # ========================================================
    # REMOVE HEADER
    # ========================================================
    def remove_header(self, key: str):
        if "headers" in self.request_data:
            self.request_data["headers"].pop(key, None)

    # ========================================================
    # EDIT BODY
    # ========================================================
    def set_body(self, body: str):
        self.request_data["body"] = body

    # ========================================================
    # ADD PARAMETER (QUERY STYLE)
    # ========================================================
    def add_param(self, key: str, value: str):
        url = self.request_data.get("url", "")

        if "?" in url:
            url += f"&{key}={value}"
        else:
            url += f"?{key}={value}"

        self.request_data["url"] = url

    # ========================================================
    # GET MODIFIED REQUEST
    # ========================================================
    def get_request(self):
        return self.request_data

    # ========================================================
    # BUILD RAW REQUEST
    # ========================================================
    def build_raw(self):
        try:
            method = self.request_data.get("method", "GET")
            url = self.request_data.get("url", "/")
            headers = self.request_data.get("headers", {})
            body = self.request_data.get("body", "")

            request_line = f"{method} {url} HTTP/1.1"

            header_text = ""
            for k, v in headers.items():
                header_text += f"{k}: {v}\n"

            raw_request = f"{request_line}\n{header_text}\n{body}"

            return raw_request

        except Exception as e:
            return f"Error building request: {str(e)}"

    # ========================================================
    # RESET REQUEST
    # ========================================================
    def reset(self):
        self.request_data = {}


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    editor = RequestEditor()

    sample = {
        "method": "GET",
        "url": "http://example.com",
        "headers": {
            "User-Agent": "CyberSuite"
        },
        "body": ""
    }

    editor.load_request(sample)

    editor.set_header("Authorization", "Bearer testtoken123")
    editor.add_param("id", "1")

    print("\n===== RAW REQUEST =====\n")
    print(editor.build_raw())