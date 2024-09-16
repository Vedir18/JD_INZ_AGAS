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
        bone = context.bone
        bone["AGAS_data"] = self.newBoneData
        return {'FINISHED'}
    
class AGAS_ListUsedSkeletonsOperator(bpy.types.Operator):
    bl_idname = "object.listusedskeletons"
    bl_label = "List used skeletons"

    def execute(self, context):
        print(GetUsedSkeletonsList())
        return {'FINISHED'}
    
def GetUsedSkeletonsList():
    skeletonsList = []
    for ob in bpy.data.objects:
        if(ob.type == "ARMATURE"):
            for bone in ob.data.bones:
                agasData = bone["AGAS_data"]
                currentSkeleton = ""
                for i in range(len(agasData)):
                    if(agasData[i]==":"):
                        if(currentSkeleton not in skeletonsList):
                            skeletonsList.append(currentSkeleton)
                        currentSkeleton = ""
                        break
                    else:
                        currentSkeleton += agasData[i]
    return skeletonsList