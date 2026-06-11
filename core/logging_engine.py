# ============================================================
# File Name : logging_engine.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Advanced Logging Engine:
# - Console + File logging
# - Structured log format
# - Log levels (INFO, WARNING, ERROR, DEBUG)
# - Component-based logging support
# ============================================================

import logging
from datetime import datetime
from pathlib import Path


class LoggingEngine:

    def __init__(self, app_name="CyberSecuritySuite", log_dir="logs"):
        self.app_name = app_name

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "application.log"

        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.DEBUG)

        self._setup_handlers()

    # ========================================================
    # SETUP LOG HANDLERS
    # ========================================================
    def _setup_handlers(self):
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # File Handler
        file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # Avoid duplicate handlers
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    # ========================================================
    # INFO LOG
    # ========================================================
    def info(self, message: str):
        self.logger.info(message)

    # ========================================================
    # WARNING LOG
    # ========================================================
    def warning(self, message: str):
        self.logger.warning(message)

    # ========================================================
    # ERROR LOG
    # ========================================================
    def error(self, message: str):
        self.logger.error(message)

    # ========================================================
    # DEBUG LOG
    # ========================================================
    def debug(self, message: str):
        self.logger.debug(message)

    # ========================================================
    # COMPONENT LOG (ADVANCED FEATURE)
    # ========================================================
    def log_component(self, component: str, message: str, level="info"):
        formatted_msg = f"[{component}] {message}"

        if level == "info":
            self.logger.info(formatted_msg)
        elif level == "warning":
            self.logger.warning(formatted_msg)
        elif level == "error":
            self.logger.error(formatted_msg)
        elif level == "debug":
            self.logger.debug(formatted_msg)

    # ========================================================
    # RAW EVENT LOGGER
    # ========================================================
    def log_event(self, event_type: str, data: dict):
        timestamp = datetime.now().isoformat()

        self.logger.info(
            f"EVENT | {event_type} | {timestamp} | {data}"
        )