import bpy

def ensure_expykit_enabled():
    addon_name = "expykit"
    if addon_name not in bpy.context.preferences.addons:
        bpy.ops.preferences.addon_enable(module=addon_name)
        print(f"Addon '{addon_name}' enabled.")
    else:
        print(f"Addon '{addon_name}' is already enabled.")

def set_expykit_bind_to(armature_name):
    armature = bpy.data.objects.get(armature_name)
    if armature and armature.type == 'ARMATURE':
        bpy.context.scene.expykit_bind_to = armature
        print(f"Set 'expykit_bind_to' to armature '{armature_name}'.")
        return True
    else:
        print(f"Armature '{armature_name}' does not exist or is not of type 'ARMATURE'.")
        return False

def run_constrain_to_armature(src_preset, trg_preset):
    # Ensure we are in Object Mode before switching to Pose Mode
    if bpy.context.object.mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')
        print(f"Switched to Pose mode.")

    # Check if we are in Pose mode and have selected exactly two armatures
    if bpy.context.mode != 'POSE' or len(bpy.context.selected_objects) != 2:
        print("Switching selection to 'root' and 'Hips' armatures.")
        
        # Ensure we are in Object Mode to select objects
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select 'root' and 'Hips' armatures
        bpy.data.objects['root'].select_set(True)
        bpy.data.objects['Hips'].select_set(True)
        
        # Set 'root' as the active object
        bpy.context.view_layer.objects.active = bpy.data.objects['root']
        
        # Switch back to Pose Mode
        bpy.ops.object.mode_set(mode='POSE')


    # Print parameters for debugging
    print(f"Running constrain with src_preset='{src_preset}' and trg_preset='{trg_preset}'")

    # Run the ConstrainToArmature operator
    try:
        bpy.ops.armature.expykit_constrain_to_armature(
            src_preset=src_preset,
            trg_preset=trg_preset,
            only_selected=False,
            bind_by_name=True,
            match_transform='Pose',
            fit_target_scale='neck',
            constraint_policy='remove',
            force_dialog=False,
        )
        print("Constrain operator executed.")
    except RuntimeError as e:
        print(f"Error executing operator: {e}")

# Ensure the Expy addon is enabled
ensure_expykit_enabled()

# Set the bind-to armature
if set_expykit_bind_to("root"):
    # Ensure we are in Pose mode and have selected the armatures
    if bpy.context.mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')

    # Run the constrain operator with the specified presets
    run_constrain_to_armature("Mixamo.py", "Rigify_Metarig.py")
else:
    print("Failed to set the bind-to armature.")
