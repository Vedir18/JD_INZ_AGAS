import bpy
from bpy.types import Context, Operator, Panel

class OBJECT_OT_AGAS_represent_armature(Operator):
    """Display example preferences"""
    bl_idname = "object.represent_armature"
    bl_label = "Addon Preferences Example Set"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        print("PRINTING BONES")
        for ob in bpy.data.objects:
            if(ob.type == "ARMATURE"):
                boneTree = BoneTree(ob)
                #context.scene.represented_bone_tree.represented_tree = boneTree
                treeText = boneTree.printTree(context)
                context.preferences.addons[__package__].preferences.bonetree = treeText
                break

        return {'FINISHED'}
    
class VIEW3D_PT_bone_tree_panel(bpy.types.Panel):
    pass
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "AGAS"
    bl_label = "AGAS bone tree panel"

    def draw(self, context):
        row = self.layout.row()
        row.operator("object.represent_armature", text="Represent Armature")
        
############# ARMATURE REPRESENTATION IN CODE #############
class BoneTree(bpy.types.Property):
    def __init__(self, armature):
        print("CREATING TREE")
        self.root = RepresentedBone(None, armature.data.bones[0])
        print("ROOT SET AS: " + self.root.blenderBone.name)
        lastBone = self.root
        for bone in armature.data.bones[1:]:
            print("   Processing bone - " + bone.name)
            print("      parrent: " + bone.parent.name + " lastBone: " + lastBone.blenderBone.name)
            while lastBone != None:
                if(bone.parent == lastBone.blenderBone):
                    print("           parrentFound")
                    break
                else:
                    print("           " + lastBone.blenderBone.name + " is not a parrent of " + bone.name + " going one up")
                    lastBone = lastBone.parent
            
            if(lastBone == None):
                print("PARENT NOT FOUND FOR: " + bone.name)
                break

            newBone = RepresentedBone(lastBone, bone)
            lastBone.children.append(newBone)
            lastBone = newBone

    def printTree(self, context):
        animListFile = open(context.preferences.addons[__package__].preferences.listFilePath, "r")
        animlistcontent = animListFile.read()
        animlist = ParseTextToWordList(animlistcontent)
        print("OPENED FILE:")
        print(animlist)
        animListFile.close
        print("PRINTING TREE")
        text = self.root.printBoneWithChildren("", animlist)
        print(text)
        return text
            

class RepresentedBone:
    def __init__(self, parent, blenderBone):
        self.parent = parent
        self.blenderBone = blenderBone
        self.children = []
    
    def printBoneWithChildren(self, indent, animlist):
        boneText = (indent+self.blenderBone.name)
        if self.blenderBone.name in animlist:
            boneText += " : FOUND"
        else:
            boneText +=" : NOT FOUND"
        #print(indent + self.blenderBone.name)
        for child in self.children:
            boneText+="\n" + child.printBoneWithChildren(indent + "-|-", animlist)
        return boneText

def ParseTextToWordList(content):
    bonelist = []
    curBoneName = ""
    for i in range(len(content)):
        if(content[i]=="\n"):
            bonelist.append(curBoneName)
            curBoneName =""
        else:
            curBoneName+=content[i]
    
    return bonelist