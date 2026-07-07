"""
Auto Damage Generator
Context utilities

Centralised Blender context validation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import bpy


@dataclass(slots=True)
class ADGContext:

    context: bpy.types.Context

    object: Optional[bpy.types.Object]

    mesh: Optional[bpy.types.Mesh]

    sculpt: Optional[bpy.types.Sculpt]

    multires: Optional[bpy.types.MultiresModifier]

    mode: str

    is_mesh: bool

    is_sculpt: bool

    has_multires: bool

    has_mask: bool

    @classmethod
    def from_context(cls, context: bpy.types.Context):

        obj = context.active_object

        mesh = obj.data if (
            obj and obj.type == 'MESH'
        ) else None

        sculpt = context.tool_settings.sculpt

        multires = None

        if obj:

            for modifier in obj.modifiers:

                if modifier.type == 'MULTIRES':

                    multires = modifier

                    break

        has_mask = False

        if mesh:

            try:

                has_mask = ".sculpt_mask" in mesh.attributes

            except Exception:

                has_mask = False

        return cls(

            context=context,

            object=obj,

            mesh=mesh,

            sculpt=sculpt,

            multires=multires,

            mode=context.mode,

            is_mesh=mesh is not None,

            is_sculpt=context.mode == "SCULPT",

            has_multires=multires is not None,

            has_mask=has_mask,
        )

    @property
    def valid(self):

        return self.is_mesh and self.is_sculpt
