import bpy

# Define the path to your FBX file
fbx_file_path = r"C:\Users\VICON\Desktop\gg_posedTo_freemocap.fbx"

# Import the FBX file with the 'automatic_bone_orientation' option enabled
bpy.ops.import_scene.fbx(filepath=fbx_file_path, automatic_bone_orientation=True)


# Apply all transforms to the imported objects
# Switch to Object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Select all imported objects
for obj in bpy.context.selected_objects:
    obj.select_set(True)

# Apply all transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
