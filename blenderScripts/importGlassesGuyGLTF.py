import bpy
import os
import json

# Function to save the bone rolls
def save_bone_rolls(armature):
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    bone_rolls = {}
    for bone in armature.data.edit_bones:
        bone_rolls[bone.name] = bone.roll
    bpy.ops.object.mode_set(mode='OBJECT')
    return bone_rolls

# Get the directory of the directory of the current script
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the relative path to your GLTF file
gltf_file_path = os.path.join(script_dir, "avatars/glassesGuyPosed.glb")
# gltf_file_path = r"C:\Users\VICON\Desktop\gg_posedTo_freemocap.glb"

# Import the GLTF file
print("Importing GLTF file...", flush=True)
bpy.ops.import_scene.gltf(
    filepath=gltf_file_path,
    import_pack_images=True,
    import_shading='NORMALS',
    guess_original_bind_pose=True,
    bone_heuristic='TEMPERANCE',
)

# Apply all transforms to the imported objects
print("Switching to Object mode...", flush=True)
bpy.ops.object.mode_set(mode='OBJECT')

# Select all imported objects
for obj in bpy.context.selected_objects:
    obj.select_set(True)

# Save bone rolls of the armature before import
original_armature = bpy.data.objects.get("glassesGuy")  # Replace "Armature" with the actual name of your armature if different
if original_armature and original_armature.type == 'ARMATURE':
    original_bone_rolls = save_bone_rolls(original_armature)
    # Save the bone rolls to a JSON file
    bone_rolls_path = os.path.join(script_dir, "bone_rolls.json")
    with open(bone_rolls_path, 'w') as f:
        json.dump(original_bone_rolls, f)
    print("Bone rolls saved to", bone_rolls_path, flush=True)
else:
    original_bone_rolls = None
    print("Original armature not found or not an armature type.", flush=True)

# Apply all transforms
print("Applying transforms...", flush=True)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
