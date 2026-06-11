# ============================================================
# File Name : url_codec.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# URL Codec Module:
# - URL encode/decode strings
# - Validate URL encoding
# - Safe handling of web parameters
# - Useful for security testing tools
# ============================================================


import urllib.parse


class URLCodec:

    # ========================================================
    # ENCODE STRING TO URL FORMAT
    # ========================================================
    def encode(self, text: str) -> str:
        try:
            return urllib.parse.quote(text)
        except Exception as e:
            return f"Encode Error: {str(e)}"

    # ========================================================
    # DECODE URL STRING
    # ========================================================
    def decode(self, encoded_text: str) -> str:
        try:
            return urllib.parse.unquote(encoded_text)
        except Exception as e:
            return f"Decode Error: {str(e)}"

    # ========================================================
    # DOUBLE ENCODE
    # ========================================================
    def double_encode(self, text: str) -> str:
        try:
            first = self.encode(text)
            return self.encode(first)
        except Exception as e:
            return f"Double Encode Error: {str(e)}"

    # ========================================================
    # DOUBLE DECODE
    # ========================================================
    def double_decode(self, encoded_text: str) -> str:
        try:
            first = self.decode(encoded_text)
            return self.decode(first)
        except Exception as e:
            return f"Double Decode Error: {str(e)}"

    # ========================================================
    # CHECK IF STRING IS URL ENCODED
    # ========================================================
    def is_encoded(self, text: str) -> bool:
        return "%" in text

    # ========================================================
    # FORMAT INFO
    # ========================================================
    def info(self, text: str):
        print("\n========== URL CODEC INFO ==========")
        print(f"Original : {text}")
        print(f"Encoded  : {self.encode(text)}")
        print(f"Decoded  : {self.decode(self.encode(text))}")
        print("====================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    codec = URLCodec()

    sample = "https://example.com/search?q=hello world"

    codec.info(sample)

    encoded = codec.encode(sample)
    print("Encoded:", encoded)

    print("Decoded:", codec.decode(encoded))