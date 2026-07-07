"""
Auto Damage Generator

Shared utility functions.
"""

from __future__ import annotations

import bpy
from datetime import datetime

# ------------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------------

DEBUG = True

_PREFIX = "[ADG]"


# ------------------------------------------------------------------------
# Logger
# ------------------------------------------------------------------------

def _timestamp() -> str:
    """Return a readable timestamp."""

    return datetime.now().strftime("%H:%M:%S")


def log(message: str) -> None:
    """General log message."""

    if DEBUG:
        print(f"{_PREFIX} [{_timestamp()}] {message}")


def info(message: str) -> None:
    """Information message."""

    if DEBUG:
        print(f"{_PREFIX} INFO    | {message}")


def warning(message: str) -> None:
    """Warning message."""

    print(f"{_PREFIX} WARNING | {message}")


def error(message: str) -> None:
    """Error message."""

    print(f"{_PREFIX} ERROR   | {message}")


# ------------------------------------------------------------------------
# Blender
# ------------------------------------------------------------------------

def blender_version() -> tuple[int, int, int]:
    """Return the running Blender version."""

    return bpy.app.version


def blender_version_string() -> str:

    version = blender_version()

    return f"{version[0]}.{version[1]}.{version[2]}"


def version_supported() -> bool:

    major, minor, _ = blender_version()

    return (major, minor) >= (5, 0)
