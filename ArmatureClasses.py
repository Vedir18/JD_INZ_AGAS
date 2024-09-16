class AGAS_Armature:
    name=""
    bones=[]
    animations=[]
    
    def __init__(self):
        self.name=""
        self.bones = []
        self.animations = []

    def PrintArmature(self):
        print("ArmatureName: " + self.name)
        print("   Bones:")
        for bone in self.bones:
            bone.PrintBone()
        print("   Animations:")
        for animation in self.animations:
            print("      " + animation)

class AGAS_Bone:
    name=""
    boneType=""
    followTypes=[]
    followBone=""

    def __init__(self):
        self.name = ""
        self.boneType = ""
        self.followTypes =[]
        self.followBone = ""

    def PrintBone(self):
        print("      BoneName: " + self.name)
        print("         type: " + self.boneType)
        print("         followTypes:")
        for followType in self.followTypes:
            print("            ft: "+followType)
        print("         followBone: "+ self.followBone)

from enum import Enum
class BoneType(Enum):
    UPPER_SPINE_START=0
    UPPER_SPINE_PART=1
    NECK_START=2
    NECK_PART=3
    HEAD=4
    UPPER_LIMB_START=5
    UPPER_LIMB_PART=6
    UPPER_HAND_START=7
    UPPER_HAND_PART=8
    LOWER_SPINE_START=9


import json
def JSON_TO_AGAS_Armatures(path):
    with open(path) as file:
        f = json.load(file)
        resultArmatures =[]
        for i in range(len(f['armatures'])):
            newArmature = AGAS_Armature()
            newArmature.name = f['armatures'][i]['armature_name']
            for j in range(len(f['armatures'][i]['bones'])):
                newBone = AGAS_Bone()
                newBone.name = f['armatures'][i]['bones'][j]['bone_name']
                newBone.boneType = f['armatures'][i]['bones'][j]['bone_type']
                for k in range(len(f['armatures'][i]['bones'][j]['follow_types'])):
                    newBone.followTypes.append(f['armatures'][i]['bones'][j]['follow_types'][k])
                newBone.followBone = f['armatures'][i]['bones'][j]['follow_bone']
                newArmature.bones.append(newBone)
            for l in range(len(f['armatures'][i]['animations'])):
                newArmature.animations.append(f['armatures'][i]['animations'][l])
            resultArmatures.append(newArmature)
        return resultArmatures
    
def AGAS_ARMATURE_TO_JSON(armatures, path):
    with open(path, 'w') as file:
        resultString = "{\"armatures\":[\n"
        for i in range(len(armatures)):
            armature=armatures[i]
            indent="    "
            resultString += indent + "{\n"
            indent2=indent+indent
            resultString += indent2 + "\"armature_name\":\""+armature.name+"\",\n"
            resultString += indent2 + "\"bones\":[\n"
            for j in range(len(armature.bones)):
                bone = armature.bones[j]
                indent4=indent2+indent2
                resultString+=indent2+indent+"{\n"
                resultString+=indent4+"\"bone_name\":\""+bone.name+"\",\n"
                resultString+=indent4+"\"bone_type\":\""+bone.boneType+"\",\n"
                resultString+=indent4+"\"follow_types\":[\n"
                for x in range(len(bone.followTypes)):
                    followType=bone.followTypes[x]
                    indent5 = indent4+indent
                    if(x < len(bone.followTypes)-1):
                        resultString+=indent5+"\""+followType+"\",\n"
                    else:
                        resultString+=indent5+"\""+followType+"\"\n"
                resultString+=indent4+"],\n"
                resultString+=indent4+"\"follow_bone\":\""+bone.followBone+"\"\n"
                if(j<len(armature.bones)-1):
                    resultString+=indent2+indent+"},\n"
                else:
                    resultString+=indent2+indent+"}\n"
            resultString+=indent2+"],\n"
            resultString+=indent2+"\"animations\":[\n"
            for y in range(len(armature.animations)):
                animation=armature.animations[y]
                if(y<len(armature.animations)-1):
                    resultString+=indent2+indent+"\""+animation+"\",\n"
                else:
                    resultString+=indent2+indent+"\""+animation+"\"\n"
            resultString+=indent2+"]\n"
            if(i<len(armatures)-1):
                resultString+=indent+"},\n"
            else:
                resultString+=indent+"}\n"
        resultString+="]}\n"
        file.write(resultString)

'''
armatures = JSON_TO_AGAS_Armatures('C:\\Users\\VED\\Desktop\\JD_AGAS\\Animations\\List.json')
for armature in armatures:
    armature.PrintArmature()
AGAS_ARMATURE_TO_JSON(armatures, 'C:\\Users\\VED\\Desktop\\JD_AGAS\\Animations\\ListResult.json')
'''