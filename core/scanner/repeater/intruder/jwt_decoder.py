# ============================================================
# File Name : jwt_decoder.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# JWT Decoder Module:
# - Decodes JWT tokens (header, payload)
# - Validates structure
# - Decodes Base64URL parts
# - Used for security analysis only
# ============================================================


import base64
import json


class JWTDecoder:

    # ========================================================
    # SAFE BASE64URL DECODE
    # ========================================================
    def _decode_base64url(self, data: str) -> dict:
        try:
            padding = "=" * (-len(data) % 4)
            decoded_bytes = base64.urlsafe_b64decode(data + padding)
            return json.loads(decoded_bytes.decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}

    # ========================================================
    # DECODE JWT TOKEN
    # ========================================================
    def decode(self, token: str) -> dict:
        try:
            parts = token.split(".")

            if len(parts) != 3:
                return {"error": "Invalid JWT format"}

            header = self._decode_base64url(parts[0])
            payload = self._decode_base64url(parts[1])
            signature = parts[2]

            return {
                "header": header,
                "payload": payload,
                "signature": signature,
                "valid_structure": True
            }

        except Exception as e:
            return {"error": str(e)}

    # ========================================================
    # VALIDATE JWT STRUCTURE
    # ========================================================
    def is_valid(self, token: str) -> bool:
        return len(token.split(".")) == 3

    # ========================================================
    # PRETTY PRINT JWT
    # ========================================================
    def info(self, token: str):
        decoded = self.decode(token)

        print("\n========== JWT DECODER ==========")

        if "error" in decoded:
            print("Error:", decoded["error"])
            return

        print("\n--- HEADER ---")
        print(json.dumps(decoded["header"], indent=4))

        print("\n--- PAYLOAD ---")
        print(json.dumps(decoded["payload"], indent=4))

        print("\n--- SIGNATURE ---")
        print(decoded["signature"])

        print("\n=================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    decoder = JWTDecoder()

    sample_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJ1c2VyIjoiZ3VsbCIsInJvbGUiOiJhZG1pbiJ9."
        "signature_part"
    )

    decoder.info(sample_token)