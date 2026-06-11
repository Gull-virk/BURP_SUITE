# ============================================================
# File Name : config.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Central configuration management module.
# Responsible for:
# - Application settings
# - Directory management
# - Logging configuration
# - Database configuration
# - Security settings
# - Report settings
# ============================================================

from pathlib import Path
from dataclasses import dataclass, field
from typing import List


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
DATA_DIR = BASE_DIR / "data"
CACHE_DIR = BASE_DIR / "cache"

for directory in [LOG_DIR, REPORT_DIR, DATA_DIR, CACHE_DIR]:
    directory.mkdir(exist_ok=True)


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

@dataclass
class ApplicationConfig:
    APP_NAME: str = "CyberSecuritySuite"
    APP_VERSION: str = "1.0.0"
    AUTHOR: str = "Gull Virk"

    DEBUG: bool = False
    VERBOSE: bool = True

    MAX_THREADS: int = 10
    REQUEST_TIMEOUT: int = 10


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

@dataclass
class LoggingConfig:
    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = str(LOG_DIR / "application.log")

    LOG_FORMAT: str = (
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

@dataclass
class DatabaseConfig:
    DATABASE_NAME: str = "cybersuite.db"

    DATABASE_PATH: str = str(
        DATA_DIR / DATABASE_NAME
    )

    ENABLE_BACKUP: bool = True


# ============================================================
# SECURITY CONFIGURATION
# ============================================================

@dataclass
class SecurityConfig:
    VERIFY_SSL: bool = True

    USER_AGENT: str = (
        "CyberSecuritySuite/1.0 "
        "(Educational Security Testing Platform)"
    )

    MAX_REDIRECTS: int = 5

    ALLOWED_PROTOCOLS: List[str] = field(
        default_factory=lambda: [
            "http",
            "https"
        ]
    )


# ============================================================
# REPORT CONFIGURATION
# ============================================================

@dataclass
class ReportConfig:
    REPORT_DIRECTORY: str = str(REPORT_DIR)

    DEFAULT_FORMAT: str = "html"

    AVAILABLE_FORMATS: List[str] = field(
        default_factory=lambda: [
            "html",
            "json",
            "txt"
        ]
    )


# ============================================================
# MODULE CONFIGURATION
# ============================================================

@dataclass
class ModuleConfig:
    ENABLE_PROXY: bool = True
    ENABLE_SCANNER: bool = True
    ENABLE_REPEATER: bool = True
    ENABLE_DECODER: bool = True
    ENABLE_REPORTS: bool = True


# ============================================================
# MASTER CONFIGURATION
# ============================================================

class Config:
    APP = ApplicationConfig()
    LOGGING = LoggingConfig()
    DATABASE = DatabaseConfig()
    SECURITY = SecurityConfig()
    REPORTS = ReportConfig()
    MODULES = ModuleConfig()


# ============================================================
# GLOBAL INSTANCE
# ============================================================

settings = Config()


# ============================================================
# TEST EXECUTION
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print(f"Application : {settings.APP.APP_NAME}")
    print(f"Version     : {settings.APP.APP_VERSION}")
    print(f"Author      : {settings.APP.AUTHOR}")
    print(f"Database    : {settings.DATABASE.DATABASE_PATH}")
    print(f"Log File    : {settings.LOGGING.LOG_FILE}")
    print(f"Reports     : {settings.REPORTS.REPORT_DIRECTORY}")
    print("=" * 60)