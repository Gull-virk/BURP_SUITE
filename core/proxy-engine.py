# ============================================================
# File Name : proxy_engine.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Educational Proxy Engine (Burp Suite style concept)
# Features:
# - Request interception (basic)
# - Logging system
# - Forwarding handler
# - Session tracking
# ============================================================

import socket
import threading
import logging
from datetime import datetime
from urllib.parse import urlparse


class ProxyEngine:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sessions = {}

        logging.basicConfig(
            filename="proxy.log",
            level=logging.INFO,
            format="%(asctime)s | %(message)s"
        )

        self.logger = logging.getLogger("ProxyEngine")

    # ========================================================
    # START PROXY SERVER
    # ========================================================
    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(100)

            print(f"[+] Proxy running on {self.host}:{self.port}")
            self.logger.info("Proxy started")

            while True:
                client_socket, addr = self.server_socket.accept()

                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, addr)
                )
                thread.start()

        except Exception as e:
            self.logger.error(f"Server error: {str(e)}")
            self.server_socket.close()

    # ========================================================
    # HANDLE CLIENT REQUEST
    # ========================================================
    def handle_client(self, client_socket, addr):
        request = client_socket.recv(4096)

        if not request:
            client_socket.close()
            return

        request_text = request.decode(errors="ignore")

        print(f"\n[REQUEST FROM] {addr}")
        print(request_text[:200])

        self.logger.info(f"Request from {addr}")

        self.log_session(addr, request_text)

        # Extract host
        first_line = request_text.split("\n")[0]
        url = first_line.split(" ")[1]

        parsed_url = urlparse(url)

        if parsed_url.hostname:
            self.forward_request(parsed_url.hostname, 80, request, client_socket)

    # ========================================================
    # FORWARD REQUEST
    # ========================================================
    def forward_request(self, host, port, request, client_socket):
        try:
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.connect((host, port))
            remote_socket.send(request)

            while True:
                response = remote_socket.recv(4096)

                if len(response) > 0:
                    client_socket.send(response)
                else:
                    break

            remote_socket.close()
            client_socket.close()

        except Exception as e:
            self.logger.error(f"Forward error: {str(e)}")
            client_socket.close()

    # ========================================================
    # SESSION LOGGING
    # ========================================================
    def log_session(self, addr, request):
        self.sessions[addr] = {
            "time": datetime.now().isoformat(),
            "request": request[:500]
        }


# ============================================================
# RUN PROXY
# ============================================================
if __name__ == "__main__":
    proxy = ProxyEngine(host="127.0.0.1", port=8080)
    proxy.start()