# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



bl_info = {
    "name" : "AGAS",
    "author" : "Jan Dziegiel",
    "description" : "",
    "blender" : (4, 1, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

# import bpy
# #from AddonProperties import AGASProperties, OBJECT_OT_AGAS_set_preferences
# #from AddonPropertiesPanel import AGAS_Panel_Properties, VIEW3D_PT_properties_panel
# from MoveEverythingOperator import MoveEverythingOperator
# from MoveEverythingPanel import MoveEverythingPanel

# classes = (
#     #AGASProperties,
#     #OBJECT_OT_AGAS_set_preferences,
#     #AGAS_Panel_Properties,
#     #VIEW3D_PT_properties_panel,
#     MoveEverythingOperator,
#     MoveEverythingPanel,
# )

# def register():
#     from bpy.utils import register_class
#     for cls in classes:
#         register_class(cls)
#     #bpy.types.Scene.agas_prop = bpy.props.PointerProperty(type=AGASProperties)
#     #bpy.types.Scene.agas_panel_prop = bpy.props.PointerProperty(type=AGAS_Panel_Properties)

# def unregister():
#     from bpy.utils import unregister_class
#     for cls in reversed(classes):
#         unregister_class(cls)
#     #del bpy.types.Scene.agas_prop
#     #del bpy.types.Scene.agas_panel_prop

# if __name__ == "__main__":
#     register()

import bpy
from .AddonPropertiesPanel import AGAS_Panel_Properties
from . import auto_load

auto_load.init()

def register():
    auto_load.register()
    bpy.types.Scene.agas_panel_prop = bpy.props.PointerProperty(type=AGAS_Panel_Properties)

def unregister():
    auto_load.unregister()
    del bpy.types.Scene.agas_panel_prop