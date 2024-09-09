import bpy
import os.path
from bpy.types import PropertyGroup
from bpy.props import EnumProperty

def GetAvailableBones(scene, context):
    items=[]
    if os.path.isfile(context.preferences.addons[__package__].preferences.animFolder+"\\List.txt"):
        boneListFile = open(context.preferences.addons[__package__].preferences.animFolder+"\\List.txt", "r")
        unparsed = boneListFile.read()
        cur = ""
        boneNr = 0
        for i in range(len(unparsed)):
            if(unparsed[i]=="\n"):
                newItem = (cur, cur, "bone nr: "+str(boneNr))
                items.append(newItem)
                boneNr += 1
                cur=""
            else:
                cur += unparsed[i]
    return items

class AGAS_CustomBonePropertyPanel_Properties(PropertyGroup):
    testPanelEnum : EnumProperty(
            items=GetAvailableBones,
            name="TestPanelEnumProp",
        )

class AGAS_CustomBonePropertyPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom bone property AGAS"
    bl_idname = "BONE_custom_prop_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "bone"    

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        chosenBone = row.prop(context.scene.agas_custombonepropertypanel_prop, "testPanelEnum")
        row = layout.row()
        boneSetter = row.operator("bone.setcustomboneproperty")
        boneSetter.newBoneData = str(context.scene.agas_custombonepropertypanel_prop.testPanelEnum)

