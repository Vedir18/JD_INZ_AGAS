import bpy
from bpy.types import Context, Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty


class AGASProperties(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    listFilePath : StringProperty(
            name="list File Path",
            subtype='FILE_PATH',
            default="MISSING FILEPATH",
            )
    
    animFolder : StringProperty(
        name="Animation Folder",
        subtype="FILE_PATH",
        default="MISSING FILEPATH",
    )

    bonetree : StringProperty(
        name="BoneTree",
        default="\n\n"
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our addon")
        layout.prop(self, "listFilePath")
        layout.prop(self, "animationsFolder")


class OBJECT_OT_AGAS_set_preferences(Operator):
    """Display example preferences"""
    bl_idname = "object.agas_set_preferences"
    bl_label = "Addon Preferences Example Set"
    bl_options = {'REGISTER', 'UNDO'}

    newPath : StringProperty(
        name="New Path",
        subtype='FILE_PATH',
        default="",
    )

    propertyID : IntProperty(
        name="PropertyID",
        default=0,
    )

    def execute(self, context):
        user_preferences = context.preferences
        addon_prefs = user_preferences.addons[__package__].preferences

        match self.propertyID:
            case 0: 
                addon_prefs.listFilePath = self.newPath
            case 1:
                addon_prefs.animFolder = self.newPath

        print("PRINTING NEW ADDON PREFS: \n listFilePath: " + addon_prefs.listFilePath + "\n animPath: " + addon_prefs.animFolder)

        return {'FINISHED'}
    
class OBJECT_OT_AGAS_import_animations(Operator):
    bl_idname = "object.importanimations"
    bl_label = "Addon Preferences Import Animation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        user_preferences = context.preferences
        addon_prefs = user_preferences.addons[__package__].preferences
        bpy.ops.import_scene.fbx( filepath = addon_prefs.animFolder )

        return {'FINISHED'}

class OBJECT_OT_AGAS_create_contraints(Operator):
    bl_idname = "object.createconstraints"
    bl_label = "AGAS create constraints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        targetArmature = scene.objects.get("HumanSkeleton")
        currentMode = context.mode
        if currentMode!='POSE':
            bpy.ops.object.mode_set(mode='POSE')

        bpy.ops.pose.select_all(action='SELECT')

        for bone in context.selected_pose_bones_from_active_object:
            bone_rotation = (bone.constraints.get("Copy Rotation") or bone.constraints.new(type='COPY_ROTATION'))
            bone_rotation.target = targetArmature
            bone_rotation.subtarget = bone.name

        bpy.ops.object.mode_set(mode=currentMode)
        return {'FINISHED'}