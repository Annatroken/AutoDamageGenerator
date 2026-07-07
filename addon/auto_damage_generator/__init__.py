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


MODULES = (
    properties,
    apply,
    preview,
    clear,
    ui,
)


def register():

    for module in MODULES:
        module.register()

    print("[ADG] Auto Damage Generator registered.")


def unregister():

    for module in reversed(MODULES):
        module.unregister()

    print("[ADG] Auto Damage Generator unregistered.")
