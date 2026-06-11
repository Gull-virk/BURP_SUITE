# ============================================================
# File Name : crawler.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Web Crawler Module:
# - Crawls web pages (authorized targets only)
# - Extracts internal/external links
# - Builds site map
# - Used for security scanning preparation
# ============================================================

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque


class WebCrawler:

    def __init__(self, base_url, max_pages=50):
        self.base_url = base_url
        self.max_pages = max_pages

        self.visited = set()
        self.queue = deque([base_url])

        self.site_map = {}

        self.headers = {
            "User-Agent": "CyberSecuritySuite-Crawler/1.0 (Educational Use Only)"
        }

    # ========================================================
    # START CRAWLING
    # ========================================================
    def crawl(self):
        while self.queue and len(self.visited) < self.max_pages:

            url = self.queue.popleft()

            if url in self.visited:
                continue

            try:
                response = requests.get(
                    url,
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code != 200:
                    continue

                self.visited.add(url)

                links = self.extract_links(response.text, url)

                self.site_map[url] = links

                for link in links:
                    if link not in self.visited:
                        self.queue.append(link)

                print(f"[CRAWLED] {url} | Links: {len(links)}")

            except Exception as e:
                print(f"[ERROR] {url} -> {str(e)}")

        return self.site_map

    # ========================================================
    # EXTRACT LINKS FROM PAGE
    # ========================================================
    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, "html.parser")

        links = set()

        for tag in soup.find_all("a", href=True):
            href = tag["href"]

            full_url = urljoin(base_url, href)

            if self.is_valid_url(full_url):
                links.add(full_url)

        return list(links)

    # ========================================================
    # CHECK VALID URL
    # ========================================================
    def is_valid_url(self, url):
        parsed = urlparse(url)

        # Only http/https allowed
        if parsed.scheme not in ["http", "https"]:
            return False

        # Stay within same domain
        base_domain = urlparse(self.base_url).netloc

        return parsed.netloc == base_domain

    # ========================================================
    # GET SITE MAP
    # ========================================================
    def get_site_map(self):
        return self.site_map


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    target = "https://example.com"

    crawler = WebCrawler(target, max_pages=20)

    site_map = crawler.crawl()

    print("\n===== SITE MAP =====")
    for page, links in site_map.items():
        print(f"\n{page}")
        for link in links:
            print(f"  -> {link}")