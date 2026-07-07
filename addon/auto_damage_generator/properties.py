# SPDX-License-Identifier: MIT
#
# Auto Damage Generator
# properties.py

from __future__ import annotations

import bpy

from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    PointerProperty,
)
from bpy.types import PropertyGroup


# ------------------------------------------------------------------------
# Global Settings
# ------------------------------------------------------------------------


class ADG_GlobalSettings(PropertyGroup):

    noise_scale: FloatProperty(
        name="Noise Scale",
        description="Scale of the procedural noise",
        default=2.5,
        min=0.01,
        soft_max=20.0,
    )

    noise_strength: FloatProperty(
        name="Noise Influence",
        description="Influence of the noise on the generated mask",
        default=0.45,
        min=0.0,
        max=1.0,
    )

    edge_threshold: FloatProperty(
        name="Edge Threshold",
        description="Minimum edge angle used for damage detection",
        default=45.0,
        min=0.0,
        max=180.0,
        subtype='ANGLE',
    )

    random_seed: IntProperty(
        name="Seed",
        default=0,
        min=0,
        max=999999,
    )


# ------------------------------------------------------------------------
# Scrape
# ------------------------------------------------------------------------


class ADG_ScrapeSettings(PropertyGroup):

    enabled: BoolProperty(
        name="Enable Scrape",
        default=True,
    )

    strength: FloatProperty(
        name="Strength",
        default=0.12,
        min=0.0,
        max=2.0,
    )

    iterations: IntProperty(
        name="Iterations",
        default=2,
        min=1,
        max=25,
    )


# ------------------------------------------------------------------------
# Crease
# ------------------------------------------------------------------------


class ADG_CreaseSettings(PropertyGroup):

    enabled: BoolProperty(
        name="Enable Crease",
        default=True,
    )

    strength: FloatProperty(
        name="Strength",
        default=0.10,
        min=0.0,
        max=2.0,
    )

    iterations: IntProperty(
        name="Iterations",
        default=1,
        min=1,
        max=25,
    )


# ------------------------------------------------------------------------
# Future Damage Types
# ------------------------------------------------------------------------


class ADG_ChipSettings(PropertyGroup):

    enabled: BoolProperty(
        name="Enable Chips",
        default=False,
    )

    density: FloatProperty(
        name="Density",
        default=0.35,
        min=0.0,
        max=1.0,
    )

    size: FloatProperty(
        name="Size",
        default=0.08,
        min=0.001,
        max=1.0,
    )


class ADG_SurfaceSettings(PropertyGroup):

    enabled: BoolProperty(
        name="Enable Surface Damage",
        default=False,
    )

    strength: FloatProperty(
        name="Strength",
        default=0.25,
        min=0.0,
        max=2.0,
    )


# ------------------------------------------------------------------------
# Preview
# ------------------------------------------------------------------------


class ADG_PreviewSettings(PropertyGroup):

    enabled: BoolProperty(
        name="Live Preview",
        default=False,
    )

    auto_update: BoolProperty(
        name="Auto Update",
        default=False,
    )


# ------------------------------------------------------------------------
# Presets
# ------------------------------------------------------------------------


class ADG_PresetSettings(PropertyGroup):

    preset: EnumProperty(
        name="Preset",
        items=[
            ("CUSTOM", "Custom", ""),
            ("STONE", "Stone", ""),
            ("WOOD", "Wood", ""),
            ("METAL", "Metal", ""),
            ("BONE", "Bone", ""),
            ("CONCRETE", "Concrete", ""),
        ],
        default="CUSTOM",
    )


# ------------------------------------------------------------------------
# Root Settings
# ------------------------------------------------------------------------


class ADG_Settings(PropertyGroup):

    global_settings: PointerProperty(
        type=ADG_GlobalSettings,
    )

    scrape: PointerProperty(
        type=ADG_ScrapeSettings,
    )

    crease: PointerProperty(
        type=ADG_CreaseSettings,
    )

    chips: PointerProperty(
        type=ADG_ChipSettings,
    )

    surface: PointerProperty(
        type=ADG_SurfaceSettings,
    )

    preview: PointerProperty(
        type=ADG_PreviewSettings,
    )

    presets: PointerProperty(
        type=ADG_PresetSettings,
    )


# ------------------------------------------------------------------------
# Registration
# ------------------------------------------------------------------------


classes = (
    ADG_GlobalSettings,
    ADG_ScrapeSettings,
    ADG_CreaseSettings,
    ADG_ChipSettings,
    ADG_SurfaceSettings,
    ADG_PreviewSettings,
    ADG_PresetSettings,
    ADG_Settings,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.adg = PointerProperty(
        type=ADG_Settings
    )


def unregister():

    del bpy.types.Scene.adg

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
