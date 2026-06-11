# ============================================================
# File Name : html.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# HTML Module:
# - Extracts links, scripts, forms
# - Cleans/sanitizes HTML
# - Basic security analysis
# - Response HTML parser utility
# ============================================================


import re
from html import escape, unescape


class HTMLProcessor:

    # ========================================================
    # CLEAN HTML (BASIC SANITIZATION)
    # ========================================================
    def clean(self, html_text: str) -> str:
        try:
            # Remove script tags
            html_text = re.sub(r"<script.*?>.*?</script>", "", html_text, flags=re.DOTALL | re.IGNORECASE)

            # Remove style tags
            html_text = re.sub(r"<style.*?>.*?</style>", "", html_text, flags=re.DOTALL | re.IGNORECASE)

            return html_text.strip()

        except Exception as e:
            return f"Clean Error: {str(e)}"

    # ========================================================
    # EXTRACT LINKS
    # ========================================================
    def extract_links(self, html_text: str):
        try:
            return re.findall(r'href=["\'](.*?)["\']', html_text, re.IGNORECASE)
        except Exception as e:
            return []

    # ========================================================
    # EXTRACT FORMS
    # ========================================================
    def extract_forms(self, html_text: str):
        try:
            return re.findall(r"<form.*?>", html_text, re.IGNORECASE)
        except Exception:
            return []

    # ========================================================
    # EXTRACT JAVASCRIPT
    # ========================================================
    def extract_scripts(self, html_text: str):
        try:
            return re.findall(r"<script.*?>.*?</script>", html_text, re.DOTALL | re.IGNORECASE)
        except Exception:
            return []

    # ========================================================
    # BASIC XSS CHECK
    # ========================================================
    def detect_xss(self, html_text: str) -> bool:
        patterns = [
            "<script",
            "javascript:",
            "onerror=",
            "onload="
        ]

        html_lower = html_text.lower()

        return any(p in html_lower for p in patterns)

    # ========================================================
    # ENCODE HTML
    # ========================================================
    def encode_html(self, text: str) -> str:
        return escape(text)

    # ========================================================
    # DECODE HTML
    # ========================================================
    def decode_html(self, text: str) -> str:
        return unescape(text)

    # ========================================================
    # SUMMARY ANALYSIS
    # ========================================================
    def analyze(self, html_text: str):

        return {
            "links": len(self.extract_links(html_text)),
            "forms": len(self.extract_forms(html_text)),
            "scripts": len(self.extract_scripts(html_text)),
            "xss_risk": self.detect_xss(html_text)
        }

    # ========================================================
    # DEBUG PRINT
    # ========================================================
    def info(self, html_text: str):

        analysis = self.analyze(html_text)

        print("\n========== HTML ANALYSIS ==========")
        print(f"Links   : {analysis['links']}")
        print(f"Forms   : {analysis['forms']}")
        print(f"Scripts : {analysis['scripts']}")
        print(f"XSS Risk: {analysis['xss_risk']}")
        print("===================================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    processor = HTMLProcessor()

    sample_html = """
    <html>
        <body>
            <a href="http://example.com">Link</a>
            <form action="/login"></form>
            <script>alert('test')</script>
        </body>
    </html>
    """

    processor.info(sample_html)