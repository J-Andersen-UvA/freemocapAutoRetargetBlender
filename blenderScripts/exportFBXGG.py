import bpy
import os

# Define the object name
object_name = "glassesGuy"

print("Starting export script...", flush=True)

# Ensure we are in Object Mode
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Get the object
obj = bpy.data.objects.get(object_name)

if obj is not None:
    print(f"Object '{object_name}' found, proceeding with export...")
    
    # Select the object
    obj.select_set(True)

    # Set the context to the object
    bpy.context.view_layer.objects.active = obj

    # Select the entire hierarchy
    bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')

    # Get the current blend file path
    blend_file_path = bpy.data.filepath
    print(f"Blend file path: {blend_file_path}")

    # Ensure the blend file is saved
    if not blend_file_path:
        raise Exception("Please save the blend file before running the script")

    # Get the directory of the blend file
    blend_dir = os.path.dirname(blend_file_path)
    print(f"Blend directory: {blend_dir}")

    # Create the out directory if it doesn't exist
    out_dir = os.path.join(blend_dir, "..", "out")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print(f"Created out directory: {out_dir}")
    else:
        print(f"Out directory already exists: {out_dir}")

    # Define the export path
    blend_filename = os.path.basename(blend_file_path)
    fbx_filename = os.path.splitext(blend_filename)[0] + ".fbx"
    export_path = os.path.join(out_dir, fbx_filename)
    print(f"Export path: {export_path}", flush=True)

    # Export selected objects to FBX
    try:
        bpy.ops.export_scene.fbx(
            filepath=export_path,
            use_selection=True,
            add_leaf_bones=False,
            bake_anim=True,
            bake_anim_use_all_actions=False,
            bake_anim_use_nla_strips=False,
            bake_anim_use_all_bones=False,
            bake_anim_force_startend_keying=False
        )
        print("Export complete", flush=True)
    except Exception as e:
        print(f"Failed to export FBX: {e}", flush=True)
else:
    print(f"Object '{object_name}' not found")

print("Script finished")
