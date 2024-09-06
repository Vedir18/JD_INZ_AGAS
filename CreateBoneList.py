import bpy

class CreateBoneListOperator(bpy.types.Operator):
    bl_idname = "object.createbonelist"
    bl_label = "Create Bone List"
    bl_options = {'REGISTER', 'UNDO'}    

    def execute(self, context):
        boneListFile = open(context.preferences.addons[__package__].preferences.listFilePath, "w")
        for ob in bpy.data.objects:
            if(ob.type == "ARMATURE"):
               for bone in ob.data.bones:
                   boneListFile.write(ob.name + ":" + bone.name + "\n")
       
        return {'FINISHED'}
    
class ListFoundSkeletonTypes(bpy.types.Operator):
    bl_idname = "object.listskeletontypes"
    bl_label = "List Skeleton Types"
    bl_options = {'REGISTER'}

    def execute(self, context):
        boneListFile = open(context.preferences.addons[__package__].preferences.listFilePath, "r")
        unparsed = boneListFile.read()
        boneList, armList = ParseToBoneList(unparsed)
        print("BONE LIST: \n")
        print(boneList)
        print("SKELETON LIST: \n")
        print(armList)
        return {'FINISHED'}
        


def ParseToBoneList(unparsed):
    boneList = []
    armList = []
    readingArmature = True
    curRead = ""
    curArm = ""
    for i in range(len(unparsed)):
        if(readingArmature):
            if(unparsed[i]==":"):
                if(curRead not in armList):
                    armList.append(curRead)
                readingArmature = False
                curArm = curRead
                curRead = ""
            else:
                curRead += unparsed[i]
        else:
            if(unparsed[i]=="\n"):
                boneList.append(curArm+":"+curRead)
                readingArmature = True
                curArm = ""
                curRead = ""
            else:
                curRead += unparsed[i]
    return boneList, armList

                