# ============================================================
# File Name : text_reports.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Text Report Generator
# - Creates TXT reports
# - Generates summaries
# - Saves findings to disk
# - Human readable output
# ============================================================

import os
from datetime import datetime


class TextReportGenerator:

    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    # ========================================================
    # GENERATE REPORT
    # ========================================================
    def generate(self, report_name, data):

       