# ============================================================
# File Name : proxy_tab.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Proxy Tab Module:
# - Simulates request interception
# - Stores intercepted traffic
# - Allows forward/drop actions
# - Proxy workflow controller
# ============================================================


from datetime import datetime


class ProxyTab:

    def __init__(self):
        self.intercept_enabled = False
        self.intercepted_requests = []

    # ========================================================
    # ENABLE/DISABLE INTERCEPT
    # ========================================================
    def toggle_intercept(self):
        self.intercept_enabled = not self.intercept_enabled
        state = "ON" if self.intercept_enabled else "OFF"
        print(f"[INTERCEPT {state}]")

    # ========================================================
    # INTERCEPT REQUEST
    # ========================================================
    def intercept(self, request: dict):

        if not self.intercept_enabled:
            return {"status": "passed", "request": request}

        intercepted = {
            "id": len(self.intercepted_requests) + 1,
            "request": request,
            "time": datetime.now().isoformat(),
            "action": "pending"
        }

        self.intercepted_requests.append(intercepted)

        print(f"[INTERCEPTED] Request ID {intercepted['id']}")

        return intercepted

    # ========================================================
    # FORWARD REQUEST
    # ========================================================
    def forward(self, request_id: int):
        for req in self.intercepted_requests:
            if req["id"] == request_id:
                req["action"] = "forwarded"
                print(f"[FORWARDED] Request ID {request_id}")
                return req

        return {"error": "Request not found"}

    # ========================================================
    # DROP REQUEST
    # ========================================================
    def drop(self, request_id: int):
        for req in self.intercepted_requests:
            if req["id"] == request_id:
                req["action"] = "dropped"
                print(f"[DROPPED] Request ID {request_id}")
                return req

        return {"error": "Request not found"}

    # ========================================================
    # VIEW HISTORY
    # ========================================================
    def history(self):
        return self.intercepted_requests

    # ========================================================
    # CLEAR HISTORY
    # ========================================================
    def clear(self):
        self.intercepted_requests = []


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    proxy = ProxyTab()

    proxy.toggle_intercept()

    proxy.intercept({"method": "GET", "url": "http://example.com"})

    proxy.intercept({"method": "POST", "url": "http://test.com/login"})

    print(proxy.forward(1))

    print(proxy.history())