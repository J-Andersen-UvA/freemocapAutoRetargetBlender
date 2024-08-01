import bpy

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Select all armatures
for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

# Switch to Pose Mode
if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
    bpy.ops.object.mode_set(mode='POSE')

# Deselect all armatures
for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        obj.select_set(False)

# Select the armature named "Hips"
hips_armature = bpy.data.objects.get("Hips")
if hips_armature and hips_armature.type == 'ARMATURE':
    hips_armature.select_set(True)
    bpy.context.view_layer.objects.active = hips_armature
