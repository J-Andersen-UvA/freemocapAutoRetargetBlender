import bpy

def ensure_action_editor():
    # Check if there is an Action Editor already
    for area in bpy.context.screen.areas:
        if area.type == 'DOPESHEET_EDITOR':
            return area

    # If not, add a new Action Editor area
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            # Split the 3D Viewport to add a new area
            region = area.regions[-1]
            bpy.ops.screen.area_split(direction='VERTICAL', factor=0.3)
            new_area = bpy.context.screen.areas[-1]
            new_area.type = 'DOPESHEET_EDITOR'
            return new_area

    print("Could not add Action Editor. Please ensure you have a VIEW_3D area to split.")
    return None

def select_armature_and_first_action(armature_name):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    
    # Find the armature object
    armature = bpy.data.objects.get(armature_name)
    if armature:
        # Select the armature
        bpy.context.view_layer.objects.active = armature
        armature.select_set(True)
    else:
        print(f"Armature named '{armature_name}' not found.")
        return
    
    # Ensure Action Editor is present
    action_editor_area = ensure_action_editor()
    if not action_editor_area:
        return

    # Check if there are any actions available
    if bpy.data.actions:
        # Select the first action in the list
        first_action = bpy.data.actions[0]
        
        # Set the mode to Action
        action_editor_area.spaces.active.mode = 'ACTION'
        
        # Set the action in the Action Editor
        if bpy.context.object.animation_data:
            bpy.context.object.animation_data.action = first_action
        else:
            print("No animation data found on the selected armature.")
    else:
        print("No actions found in the scene.")

    # Refresh the view
    bpy.context.view_layer.update()

# Specify the armature name
armature_name = "root"

# Run the function
select_armature_and_first_action(armature_name)
