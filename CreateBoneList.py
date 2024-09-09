import bpy
import glob, os

class CreateBoneListOperator(bpy.types.Operator):
    bl_idname = "object.createbonelist"
    bl_label = "Create Bone List"
    bl_options = {'REGISTER', 'UNDO'}    

    def execute(self, context):
        #clear existing file
        boneListFile = open(context.preferences.addons[__package__].preferences.animFolder+"\\List.txt", "w")
        boneListFile.write("")
        boneListFile.close

        #find fbx files
        animFolderPath = context.preferences.addons[__package__].preferences.animFolder
        filesInPath = os.listdir(animFolderPath)
        fbxFiles = []
        for file in filesInPath:
            if(file.endswith(".fbx")):
                fbxFiles.append(animFolderPath+"\\"+file)
        print(fbxFiles)

        #import add to bone list and delete
        for fbxFile in fbxFiles:
            bpy.ops.import_scene.fbx(filepath=fbxFile)
            importedObject = bpy.ops.object
            AddToBoneList(context.preferences.addons[__package__].preferences.animFolder+"\\List.txt")
            importedObject.delete(use_global=False)

        return {'FINISHED'}
    
def AddToBoneList(listFilePath):
    boneListFile = open(listFilePath, "a")
    armature = bpy.context.selected_objects[0]
    if(armature.type == "ARMATURE"):
        for bone in armature.data.bones:
            boneListFile.write(armature.name + ":" + bone.name + "\n")
    boneListFile.close

class ListFoundSkeletonTypes(bpy.types.Operator):
    bl_idname = "object.listskeletontypes"
    bl_label = "List Skeleton Types"
    bl_options = {'REGISTER'}

    def execute(self, context):
        boneListFile = open(context.preferences.addons[__package__].preferences.animFolder+"\\List.txt", "r")
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

                