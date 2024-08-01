import bpy

def bake_constrained_actions(armature_name):
    # Check if the specified armature exists in the scene
    armature = bpy.data.objects.get(armature_name)
    if not armature or armature.type != 'ARMATURE':
        print(f"Armature '{armature_name}' not found or is not an armature.")
        return

    # Ensure we are in OBJECT mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the specified armature
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature

    # Ensure we are in Pose Mode
    bpy.ops.object.mode_set(mode='POSE')

    # Set the properties directly on the operator and execute it
    bpy.ops.armature.expykit_bake_constrained_actions(
        'INVOKE_DEFAULT',
        clear_users_old=True,
        fake_user_new=True,
        exclude_deform=True,
        do_bake=True
    )


# Example usage
bake_constrained_actions("Hips")
