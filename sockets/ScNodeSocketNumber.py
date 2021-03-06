import bpy

from bpy.props import FloatProperty, StringProperty
from bpy.types import NodeSocket
from ._base.socket_base import ScNodeSocket

class ScNodeSocketNumber(NodeSocket, ScNodeSocket):
    bl_idname = "ScNodeSocketNumber"
    bl_label = "Number"
    color = (0.0, 1.0, 0.0, 1.0)

    default_value: FloatProperty()
    default_type: StringProperty(default="NUMBER")

    def get_label(self):
        return str(round(self.default_value, 2))