# ============================================================
# File Name : text_scanner.py
# Description:
# Text Analysis Module
# ============================================================

import re


class TextScanner:

    def __init__(self):
        self.results = {}

    def count_words(self, text):
        return len(text.split())

    def count_characters(self, text):
        return len(text)

    def extract_emails(self, text):
        pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        return re.findall(pattern, text)

    def extract_urls(self, text):
        pattern = r'https?://[^\s]+'
        return re.findall(pattern, text)

    def analyze(self, text):
        self.results = {
            "words": self.count_words(text),
            "characters": self.count_characters(text),
            "emails": self.extract_emails(text),
            "urls": self.extract_urls(text)
        }
        return self.results


if __name__ == "__main__":

    scanner = TextScanner()

    sample_text = """
    Contact: admin@example.com
    Website: https://example.com
    """

    print(scanner.analyze(sample_text))