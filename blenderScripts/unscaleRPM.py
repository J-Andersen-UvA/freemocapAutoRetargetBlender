import bpy

def unscale_target_armature(target_armature_name):
    target_armature = bpy.data.objects[target_armature_name]
    if "initial_scale_factor" in target_armature:
        unscale_factor = target_armature["initial_scale_factor"]
        target_armature.scale *= unscale_factor

        # Set the target armature as the active object and select it
        bpy.context.view_layer.objects.active = target_armature
        target_armature.select_set(True)
        
        # Apply scale to make it permanent
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        print(f"Unscaled {target_armature_name} by a factor of {unscale_factor} to revert to its original size", flush=True)
    else:
        print(f"No initial scale factor found for {target_armature_name}. Cannot unscale.", flush=True)


# Define the object name
object_name = "glassesGuy"

print("Starting unscale script...", flush=True)

# Ensure we are in Object Mode
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Get the object
obj = bpy.data.objects.get(object_name)

# Example usage to unscale:
target_armature_name = "Hips"  # Replace with your target armature name
unscale_target_armature(target_armature_name)
