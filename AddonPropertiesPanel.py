import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty

class AGAS_Panel_Properties(PropertyGroup):
    
    path: StringProperty(
        name="NewPath",
        description=":",
        default="",
        maxlen=1024,
    )

class VIEW3D_PT_properties_panel(bpy.types.Panel):
    pass
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "AGAS"
    bl_label = "AGAS properties panel"

    def draw(self, context):
        addonprefs=context.preferences.addons[__package__].preferences
        addonFilepath = addonprefs.listFilePath
        addonAnimationsFolder = addonprefs.animFolder
        row = self.layout.row()
        row.label(text="Filepath: " + addonFilepath)
        row = self.layout.row()
        row.label(text="AnimationsFolder: " + addonAnimationsFolder)
        row = self.layout.row()
        row.prop(context.scene.agas_panel_prop, "path")
        row = self.layout.row()
        listSetter = row.operator("object.agas_set_preferences", text="SetListFilePath")
        listSetter.newPath = context.scene.agas_panel_prop.path
        listSetter.propertyID = 0
        row = self.layout.row()
        animSetter = row.operator("object.agas_set_preferences", text="Set AnimFolder")
        animSetter.newPath = context.scene.agas_panel_prop.path
        animSetter.propertyID = 1
        row = self.layout.row()
        row.operator("object.createbonelist", text="Create Bone List")
        row = self.layout.row()
        row.operator("object.listskeletontypes", text="List Skeleton Types")
        row = self.layout.row()
        row.operator("object.importanimations", text="Import Animations")
        row = self.layout.row()
        row.operator("object.createconstraints", text="Copy animations")

        row = self.layout.row()
        row.label(text="")
        ParseText(self, addonprefs.bonetree)

def ParseText(self, text):
    currentLine = ""
    for i in range(len(text)):
        if(text[i]=="\n"):
            row = self.layout.row()
            row.label(text=currentLine)
            currentLine=""
        else:
            currentLine+=text[i]
    row = self.layout.row()
    row.label(text=currentLine)
