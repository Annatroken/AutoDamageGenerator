"""
Auto Damage Generator

Central logging system.

All modules should use this logger instead of print().
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

import bpy


# ------------------------------------------------------------------------
# Log Levels
# ------------------------------------------------------------------------


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3


# ------------------------------------------------------------------------
# Logger
# ------------------------------------------------------------------------


class ADGLogger:
    """
    Central logger used throughout the entire addon.
    """

    def __init__(self) -> None:

        self.level = LogLevel.INFO

        self.enabled = True

    # ----------------------------------------------------------

    def _time(self) -> str:

        return datetime.now().strftime("%H:%M:%S")

    # ----------------------------------------------------------

    def _print(
        self,
        level: LogLevel,
        message: str,
    ) -> None:

        if not self.enabled:
            return

        if level.value < self.level.value:
            return

        print(
            f"[ADG] "
            f"{self._time()} "
            f"{level.name:<7} "
            f"{message}"
        )

    # ----------------------------------------------------------

    def debug(self, message: str) -> None:

        self._print(LogLevel.DEBUG, message)

    # ----------------------------------------------------------

    def info(self, message: str) -> None:

        self._print(LogLevel.INFO, message)

    # ----------------------------------------------------------

    def warning(self, message: str) -> None:

        self._print(LogLevel.WARNING, message)

    # ----------------------------------------------------------

    def error(self, message: str) -> None:

        self._print(LogLevel.ERROR, message)

    # ----------------------------------------------------------

    def separator(self) -> None:

        if self.enabled:

            print("-" * 70)

    # ----------------------------------------------------------

    def blender_info(self) -> None:

        version = bpy.app.version

        self.info(
            f"Running Blender "
            f"{version[0]}.{version[1]}.{version[2]}"
        )

    # ----------------------------------------------------------

    def performance(
        self,
        task: str,
        milliseconds: float,
    ) -> None:

        self.debug(
            f"{task}: "
            f"{milliseconds:.3f} ms"
        )


# ------------------------------------------------------------------------
# Global Logger Instance
# ------------------------------------------------------------------------


LOGGER = ADGLogger()
