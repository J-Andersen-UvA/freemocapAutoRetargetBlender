# This is a blender script to call the freemocap adapter with the add rig functionality
import bpy
import sys
from pathlib import Path

# Set the path to the freemocap addon
freemocap_path = "freemocap_adapter"
sys.path.append(freemocap_path)

# Enable the freemocap addon
if "freemocap_adapter" not in bpy.context.preferences.addons:
    bpy.ops.preferences.addon_enable(module="freemocap_adapter")

# Set the add_rig parameters
bpy.context.scene.fmc_adapter_tool.add_rig_method = "bone_by_bone"
bpy.context.scene.fmc_adapter_tool.armature_name = "FreeMoCap"
bpy.context.scene.fmc_adapter_tool.add_fingers_constraints = True
bpy.context.scene.fmc_adapter_tool.ik_transition_threshold = 0.9

# Call the add_rig operator
bpy.ops.fmc_adapter.add_rig()
