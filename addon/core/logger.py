"""
Central logging for Auto Damage Generator.
"""

from __future__ import annotations

import logging
from contextlib import contextmanager
from time import perf_counter

LOGGER_NAME = "AutoDamageGenerator"

LOGGER = logging.getLogger(LOGGER_NAME)

if not LOGGER.handlers:

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[ADG] %(levelname)-8s %(message)s"
    )

    handler.setFormatter(formatter)

    LOGGER.addHandler(handler)

LOGGER.setLevel(logging.INFO)

LOGGER.propagate = False


@contextmanager
def timer(name: str):

    start = perf_counter()

    try:

        yield

    finally:

        duration = (perf_counter() - start) * 1000.0

        LOGGER.debug(
            "%s finished in %.2f ms",
            name,
            duration,
        )
