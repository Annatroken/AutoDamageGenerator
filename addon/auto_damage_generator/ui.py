# SPDX-License-Identifier: MIT
#
# Auto Damage Generator
# ui.py

from __future__ import annotations

import bpy

from bpy.types import Panel


class ADG_PT_main_panel(Panel):
    """Main UI panel."""

    bl_label = "Auto Damage Generator"
    bl_idname = "ADG_PT_main_panel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Auto Damage"

    @classmethod
    def poll(cls, context):

        obj = context.active_object

        return (
            obj is not None
            and obj.type == "MESH"
        )

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        settings = scene.adg

        # ----------------------------------------------------
        # Global
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Global")

        global_settings = settings.global_settings

        box.prop(global_settings, "noise_scale")
        box.prop(global_settings, "noise_strength")
        box.prop(global_settings, "edge_threshold")
        box.prop(global_settings, "random_seed")

        # ----------------------------------------------------
        # Scrape
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Scrape")

        scrape = settings.scrape

        box.prop(scrape, "enabled")

        col = box.column()
        col.enabled = scrape.enabled

        col.prop(scrape, "strength")
        col.prop(scrape, "iterations")

        # ----------------------------------------------------
        # Crease
        # ----------------------------------------------------

        box = layout.box()

        box.label(text="Crease")

        crease = settings.crease

        box.prop(crease, "enabled")

        col = box.column()
        col.enabled = crease.enabled

        col.prop(crease, "strength")
        col.prop(crease, "iterations")

        # ----------------------------------------------------
        # Execute
        # ----------------------------------------------------

        layout.separator()

        layout.operator(
            "adg.apply_damage",
            icon="SCULPTMODE_HLT",
        )


classes = (
    ADG_PT_main_panel,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
