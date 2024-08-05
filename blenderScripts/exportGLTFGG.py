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
    gltf_filename = os.path.splitext(blend_filename)[0] + ".glb"
    export_path = os.path.join(out_dir, gltf_filename)
    print(f"Export path: {export_path}", flush=True)

    # Export selected objects to GLTF
    try:
        bpy.ops.export_scene.gltf(
            filepath=export_path,
            use_selection=True,
            export_format='GLB',  # 'GLB' for binary format, 'GLTF_SEPARATE' for separate files
            export_apply=True,  # Apply transformations
            export_materials='EXPORT',  # Export materials
            export_texture_dir=out_dir,  # Directory for textures if 'GLTF_SEPARATE'
            export_colors=True,  # Export vertex colors
            export_draco_mesh_compression_enable=False,  # Enable Draco compression (optional)
            export_extras=False,  # Export extra data
            export_cameras=False,  # Export cameras
            export_lights=False  # Export lights
        )
        print("Export complete", flush=True)
    except Exception as e:
        print(f"Failed to export GLTF: {e}", flush=True)
else:
    print(f"Object '{object_name}' not found")

print("Script finished")
