import bpy
import time

def bake_constrained_actions(armature_name):
    print(f"Baking constrained actions for armature '{armature_name}'...", flush=True)
    armature = bpy.data.objects.get(armature_name)
    if not armature or armature.type != 'ARMATURE':
        print(f"Armature '{armature_name}' not found or is not an armature.")
        return

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')

    bpy.ops.armature.expykit_bake_constrained_actions(
        'INVOKE_DEFAULT',
        clear_users_old=True,
        fake_user_new=True,
        exclude_deform=True,
        do_bake=True
    )

def is_animation_baked(armature_name):
    armature = bpy.data.objects.get(armature_name)
    if not armature or not armature.animation_data:
        return False
    
    print(f"Checking if animation is baked for armature '{armature_name}'...", flush=True)
    return armature.animation_data.action is not None

def wait_for_bake_completion(armature_name, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if is_animation_baked(armature_name):
            return True
        time.sleep(0.5)
    return False

def ensure_action_editor():
    for area in bpy.context.screen.areas:
        if area.type == 'DOPESHEET_EDITOR':
            return area

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            bpy.ops.screen.area_split(direction='VERTICAL', factor=0.3)
            new_area = bpy.context.screen.areas[-1]
            new_area.type = 'DOPESHEET_EDITOR'
            return new_area

    print("Could not add Action Editor. Please ensure you have a VIEW_3D area to split.")
    return None

def switch_to_object_mode():
    if bpy.context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

def switch_to_pose_mode():
    if bpy.context.object.mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')

def select_armature_and_action_by_name(armature_name, action_name):
    switch_to_object_mode()
    bpy.ops.object.select_all(action='DESELECT')
    armature = bpy.data.objects.get(armature_name)
    if armature:
        bpy.context.view_layer.objects.active = armature
        armature.select_set(True)

        if not armature.animation_data:
            armature.animation_data_create()

        action_editor_area = ensure_action_editor()
        if not action_editor_area:
            return

        action = bpy.data.actions.get(action_name)
        if action:
            action_editor_area.spaces.active.mode = 'ACTION'
            switch_to_pose_mode()
            armature.animation_data.action = action
        else:
            print(f"Action named '{action_name}' not found.")
    else:
        print(f"Armature named '{armature_name}' not found.")

    bpy.context.view_layer.update()

# Main script
armature_name = "Hips"
action_name = "Action.001"

bake_constrained_actions(armature_name)
if wait_for_bake_completion(armature_name):
    select_armature_and_action_by_name(armature_name, action_name)
else:
    print("Timeout waiting for animation bake to complete.", flush=True)
