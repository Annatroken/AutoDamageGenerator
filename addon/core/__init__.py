# SPDX-License-Identifier: MIT
#
# Auto Damage Generator
# Blender 5.x Add-on
#
# Author: Gregor Petzke & OpenAI
#
# __init__.py

bl_info = {
    "name": "Auto Damage Generator",
    "author": "Gregor Petzke, OpenAI",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Auto Damage",
    "description": (
        "Procedural edge wear, scrape and crease generator "
        "for Multires sculpting."
    ),
    "category": "Sculpt",
}


import bpy

from . import properties
from . import ui

from .operators import apply
from .operators import preview
from .operators import clear

from .core import utils


MODULES = (
    properties,
    apply,
    preview,
    clear,
    ui,
)


def register():
    """Register all addon modules."""

    utils.info("Registering Auto Damage Generator")
    utils.info(
        f"Running on Blender {utils.blender_version_string()}"
    )

    for module in MODULES:
        try:
            module.register()
            utils.info(f"Registered: {module.__name__}")
        except Exception as exc:
            utils.error(f"Failed to register {module.__name__}: {exc}")
            raise

    utils.info("Registration successful")
    

def unregister():
    """Unregister all addon modules."""

    utils.info("Unregistering Auto Damage Generator")

    for module in reversed(MODULES):
        try:
            module.unregister()
            utils.info(f"Unregistered: {module.__name__}")
        except Exception as exc:
            utils.error(f"Failed to unregister {module.__name__}: {exc}")
            raise

    utils.info("Addon unloaded")
