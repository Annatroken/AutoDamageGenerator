from __future__ import annotations

import bpy

from bpy.types import Operator

from ..core.engine import DamageEngine
from ..core.logger import LOGGER


class ADG_OT_apply_damage(Operator):
    """Apply procedural damage"""

    bl_idname = "adg.apply_damage"
    bl_label = "Apply Damage"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        obj = context.active_object

        return (
            obj is not None
            and obj.type == "MESH"
            and context.mode == "SCULPT"
        )

    def execute(self, context):

        try:

            engine = DamageEngine(context)

            engine.execute()

            self.report(
                {'INFO'},
                "Auto Damage executed."
            )

            return {'FINISHED'}

        except Exception as exc:

            LOGGER.exception(exc)

            self.report(
                {'ERROR'},
                str(exc)
            )

            return {'CANCELLED'}


classes = (
    ADG_OT_apply_damage,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
