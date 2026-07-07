"""
Custom exceptions for Auto Damage Generator.
"""

from __future__ import annotations


class ADGError(Exception):
    """Base exception for all user-facing addon errors."""


class InvalidContextError(ADGError):
    """Raised when Blender is in an invalid context."""


class MultiresRequiredError(ADGError):
    """Raised when an operation requires a Multires modifier."""


class MaskGenerationError(ADGError):
    """Raised when mask generation fails."""
