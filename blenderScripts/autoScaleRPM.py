import bpy

def get_shoulder_height(armature_name, left_shoulder_bone, right_shoulder_bone):
    armature = bpy.data.objects[armature_name]
    left_shoulder = armature.pose.bones[left_shoulder_bone].head.z
    right_shoulder = armature.pose.bones[right_shoulder_bone].head.z
    return (left_shoulder + right_shoulder) / 2

# Replace these with the names of your armatures and shoulder bones
source_armature_name = "root"
target_armature_name = "Hips"
target_left_shoulder_bone_name = "LeftShoulder"
target_right_shoulder_bone_name = "RightShoulder"
source_left_shoulder_bone_name = "shoulder.L"
source_right_shoulder_bone_name = "shoulder.R"

source_shoulder_height = get_shoulder_height(source_armature_name, source_left_shoulder_bone_name, source_right_shoulder_bone_name)
target_shoulder_height = get_shoulder_height(target_armature_name, target_left_shoulder_bone_name, target_right_shoulder_bone_name)

# Calculate the scale factor
scale_factor = source_shoulder_height / target_shoulder_height

# Scale the target armature
target_armature = bpy.data.objects[target_armature_name]
initial_scale = target_armature.scale.copy()  # Store the initial scale

target_armature.scale *= scale_factor

# Apply scale to make it permanent
bpy.context.view_layer.objects.active = target_armature
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

print(f"Scaled {target_armature_name} by a factor of {scale_factor} to match the shoulder height of {source_armature_name}", flush=True)

# Save the initial scale factor to a property for later use
target_armature["initial_scale_factor"] = 1 / scale_factor
