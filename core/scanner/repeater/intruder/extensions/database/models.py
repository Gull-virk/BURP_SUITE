# ============================================================
# File Name : models.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Models Module:
# - Defines core data structures
# - Request / Response / Vulnerability models
# - Standardizes internal data flow
# ============================================================


from datetime import datetime


# ============================================================
# REQUEST MODEL
# ============================================================
class RequestModel:

    def __init__(self, method="GET", url="", headers=None, body=""):
        self.method = method.upper()
        self.url = url
        self.headers = headers if headers else {}
        self.body = body
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "method": self.method,
            "url": self.url,
            "headers": self.headers,
            "body": self.body,
            "timestamp": self.timestamp
        }


# ============================================================
# RESPONSE MODEL
# ============================================================
class ResponseModel:

    def __init__(self, status_code=0, headers=None, body=""):
        self.status_code = status_code
        self.headers = headers if headers else {}
        self.body = body
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "headers": self.headers,
            "body": self.body,
            "timestamp": self.timestamp
        }


# ============================================================
# VULNERABILITY MODEL
# ============================================================
class VulnerabilityModel:

    def __init__(self, vtype, severity, url="", payload="", evidence=""):
        self.type = vtype
        self.severity = severity
        self.url = url
        self.payload = payload
        self.evidence = evidence
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "type": self.type,
            "severity": self.severity,
            "url": self.url,
            "payload": self.payload,
            "evidence": self.evidence,
            "timestamp": self.timestamp
        }


# ============================================================
# SCAN SESSION MODEL
# ============================================================
class ScanSessionModel:

    def __init__(self, target):
        self.target = target
        self.start_time = datetime.now().isoformat()
        self.end_time = None
        self.results = []

    def add_result(self, result: dict):
        self.results.append(result)

    def end_session(self):
        self.end_time = datetime.now().isoformat()

    def to_dict(self):
        return {
            "target": self.target,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "results": self.results
        }


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    req = RequestModel("GET", "http://example.com")
    res = ResponseModel(200, {"Server": "CyberSuite"}, "OK")
    vuln = VulnerabilityModel("XSS", "High", "http://test.com", "<script>", "reflected")

    session = ScanSessionModel("http://example.com")
    session.add_result(vuln.to_dict())
    session.end_session()

    print(req.to_dict())
    print(res.to_dict())
    print(vuln.to_dict())
    print(session.to_dict())