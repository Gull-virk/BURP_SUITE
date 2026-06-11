# ============================================================
# File Name : base64_manager.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Base64 Manager Module:
# - Encode text to Base64
# - Decode Base64 to text
# - Validate Base64 strings
# - Safe utility for security tools
# ============================================================


import base64


class Base64Manager:

    # ========================================================
    # ENCODE STRING TO BASE64
    # ========================================================
    def encode(self, text: str) -> str:
        try:
            encoded_bytes = base64.b64encode(text.encode("utf-8"))
            return encoded_bytes.decode("utf-8")
        except Exception as e:
            return f"Encode Error: {str(e)}"

    # ========================================================
    # DECODE BASE64 TO STRING
    # ========================================================
    def decode(self, encoded_text: str) -> str:
        try:
            decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
            return decoded_bytes.decode("utf-8")
        except Exception as e:
            return f"Decode Error: {str(e)}"

    # ========================================================
    # VALIDATE BASE64 STRING
    # ========================================================
    def is_valid(self, encoded_text: str) -> bool:
        try:
            base64.b64decode(encoded_text, validate=True)
            return True
        except Exception:
            return False

    # ========================================================
    # DOUBLE ENCODE (ADVANCED FEATURE)
    # ========================================================
    def double_encode(self, text: str) -> str:
        first = self.encode(text)
        return self.encode(first)

    # ========================================================
    # DOUBLE DECODE (ADVANCED FEATURE)
    # ========================================================
    def double_decode(self, encoded_text: str) -> str:
        first = self.decode(encoded_text)
        return self.decode(first)

    # ========================================================
    # PRINT INFO
    # ========================================================
    def info(self, text: str):
        print("\n========== BASE64 INFO ==========")
        print(f"Original : {text}")
        print(f"Encoded  : {self.encode(text)}")
        print("=================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    manager = Base64Manager()

    sample = "CyberSecuritySuite"

    manager.info(sample)

    encoded = manager.encode(sample)
    print("Decoded:", manager.decode(encoded))