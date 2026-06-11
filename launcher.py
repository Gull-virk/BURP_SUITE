# ============================================================
# File Name : launcher.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Description:
# Main application launcher responsible for:
# - Environment validation
# - Configuration loading
# - Logging initialization
# - Module startup
# - Graceful shutdown handling
# ============================================================

import sys
import signal
import logging
from pathlib import Path
from datetime import datetime

APP_NAME = "CyberSecuritySuite"
APP_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "application.log"


def setup_logging():
    """Initialize logging system."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger(APP_NAME)
    logger.info("=" * 60)
    logger.info(f"{APP_NAME} v{APP_VERSION} Starting")
    logger.info("=" * 60)

    return logger


def validate_environment(logger):
    """Validate runtime environment."""

    logger.info("Validating environment...")

    if sys.version_info < (3, 10):
        logger.error("Python 3.10 or higher is required.")
        sys.exit(1)

    logger.info("Environment validation completed.")


def load_configuration(logger):
    """Load application configuration."""

    logger.info("Loading configuration...")

    config = {
        "debug": False,
        "startup_time": datetime.now().isoformat(),
        "modules": [
            "proxy",
            "scanner",
            "repeater",
            "decoder",
            "reports"
        ]
    }

    logger.info("Configuration loaded successfully.")
    return config


def initialize_modules(config, logger):
    """Initialize project modules."""

    logger.info("Initializing modules...")

    for module in config["modules"]:
        logger.info(f"Loaded module: {module}")

    logger.info("All modules initialized.")


def shutdown_handler(signum, frame):
    """Graceful shutdown."""

    logging.getLogger(APP_NAME).info(
        f"Shutdown signal received ({signum})."
    )

    logging.getLogger(APP_NAME).info(
        "Application terminated safely."
    )

    sys.exit(0)


def register_signals():
    """Register OS signals."""

    signal.signal(signal.SIGINT, shutdown_handler)

    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, shutdown_handler)


def print_banner():
    banner = rf"""

   _____      _                _____
  / ____|    | |              / ____|
 | |    _   _| |__   ___ _ __| (___
 | |   | | | | '_ \ / _ \ '__|\___ \
 | |___| |_| | |_) |  __/ |   ____) |
  \_____\__, |_.__/ \___|_|  |_____/
         __/ |
        |___/

     CyberSecuritySuite v{APP_VERSION}

    """

    print(banner)


def main():
    print_banner()

    logger = setup_logging()

    register_signals()

    validate_environment(logger)

    config = load_configuration(logger)

    initialize_modules(config, logger)

    logger.info("Application started successfully.")
    logger.info("System ready.")

    try:
        while True:
            pass

    except KeyboardInterrupt:
        shutdown_handler(signal.SIGINT, None)


if __name__ == "__main__":
    main()