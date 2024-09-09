import bpy
from bpy.props import StringProperty

class AGAS_SetCustomBonePropertyOperator(bpy.types.Operator):
    bl_idname = "bone.setcustomboneproperty"
    bl_label = "Set custom bone propety"
    bl_options = {'REGISTER', 'UNDO'}    

    newBoneData : StringProperty(
        name="New Data",
        default="",
    )

    def execute(self, context):
        bone = context.edit_bone
        bone["AGAS_data"] = self.newBoneData
        return {'FINISHED'}