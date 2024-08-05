import bpy
import os
import json

# Function to restore the bone rolls
def restore_bone_rolls(armature, bone_rolls):
    for bone_name, roll in bone_rolls.items():
        bone = armature.data.bones.get(bone_name)
        if bone:
            bone.roll = roll

# Get the directory of the directory of the current script
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the bone rolls from the JSON file
bone_rolls_path = os.path.join(script_dir, "bone_rolls.json")
with open(bone_rolls_path, 'r') as f:
    bone_rolls = json.load(f)
print("Bone rolls loaded from", bone_rolls_path)

# Restore bone rolls to the armature
original_armature = bpy.data.objects.get("Armature")  # Replace "Armature" with the actual name of your armature
if original_armature and original_armature.type == 'ARMATURE':
    restore_bone_rolls(original_armature, bone_rolls)
    print("Bone rolls have been restored.")
else:
    print("Original armature not found or not an armature type.")
