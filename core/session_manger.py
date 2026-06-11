# ============================================================
# File Name : session_manager.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Session Manager Module:
# - Tracks client sessions
# - Stores request/response history
# - Manages session lifecycle
# - Provides session analytics
# ============================================================

from datetime import datetime
import uuid


class SessionManager:

    def __init__(self):
        self.sessions = {}

    # ========================================================
    # CREATE NEW SESSION
    # ========================================================
    def create_session(self, client_ip: str):
        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "client_ip": client_ip,
            "created_at": datetime.now().isoformat(),
            "requests": [],
            "responses": [],
            "status": "active"
        }

        return session_id

    # ========================================================
    # ADD REQUEST TO SESSION
    # ========================================================
    def add_request(self, session_id: str, request_data: dict):
        if session_id in self.sessions:
            self.sessions[session_id]["requests"].append({
                "time": datetime.now().isoformat(),
                "data": request_data
            })

    # ========================================================
    # ADD RESPONSE TO SESSION
    # ========================================================
    def add_response(self, session_id: str, response_data: dict):
        if session_id in self.sessions:
            self.sessions[session_id]["responses"].append({
                "time": datetime.now().isoformat(),
                "data": response_data
            })

    # ========================================================
    # GET SESSION DATA
    # ========================================================
    def get_session(self, session_id: str):
        return self.sessions.get(session_id, None)

    # ========================================================
    # CLOSE SESSION
    # ========================================================
    def close_session(self, session_id: str):
        if session_id in self.sessions:
            self.sessions[session_id]["status"] = "closed"
            self.sessions[session_id]["closed_at"] = datetime.now().isoformat()

    # ========================================================
    # LIST ALL SESSIONS
    # ========================================================
    def list_sessions(self):
        return {
            sid: {
                "client_ip": data["client_ip"],
                "status": data["status"],
                "created_at": data["created_at"]
            }
            for sid, data in self.sessions.items()
        }

    # ========================================================
    # SESSION ANALYTICS
    # ========================================================
    def session_summary(self, session_id: str):
        session = self.sessions.get(session_id)

        if not session:
            return {"error": "Session not found"}

        return {
            "session_id": session_id,
            "client_ip": session["client_ip"],
            "total_requests": len(session["requests"]),
            "total_responses": len(session["responses"]),
            "status": session["status"],
            "duration": {
                "created_at": session["created_at"],
                "closed_at": session.get("closed_at", "still active")
            }
        }