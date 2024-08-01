import os
import subprocess

# Set the path to the Blender executable
blender_executable = "C:/Program Files/Blender Foundation/Blender 4.0/blender.exe"

# Set the path to the blend files
blend_files_path = "D:/Freemocap/in"

# Set the path to the exported files
exported_files_path = "D:/Freemocap/out"

# Set the path to the freemocap addon
freemocap_addon_name = "freemocap_adapter"

# Function to generate the export script
def generate_export_script(exported_files_path):
    return f"""
import bpy
import sys
from pathlib import Path

# Set the path to the freemocap addon
freemocap_path = "{freemocap_addon_name}"
sys.path.append(freemocap_path)

# Enable the freemocap addon
if "{freemocap_addon_name}" not in bpy.context.preferences.addons:
    bpy.ops.preferences.addon_enable(module="{freemocap_addon_name}")

# Export the FBX file with a default name
bpy.ops.fmc_adapter.export_fbx()

# Print the actual export path
print("Export path:", Path("{exported_files_path}") / 'FBX' / 'fmc_export.fbx')

# Quit Blender
bpy.ops.wm.quit_blender()
"""

# Iterate over the blend files
for file_name in os.listdir(blend_files_path):
    if file_name.endswith(".blend"):
        print(f"Found .blend file: {file_name}")
        
        # Define the file paths
        blend_file_path = os.path.join(blend_files_path, file_name)
        temp_fbx_file_path = os.path.join(blend_files_path, "FBX", "fmc_export.fbx")
        final_fbx_file_path = os.path.join(exported_files_path, os.path.splitext(file_name)[0] + ".fbx")
        
        # Generate the export script content
        script_content = generate_export_script(exported_files_path)
        
        # Write the export script to a temporary file
        script_path = os.path.join(blend_files_path, "temp_export_script.py")
        with open(script_path, "w") as script_file:
            script_file.write(script_content)

        # Run Blender with the export script
        subprocess.run([blender_executable, "--background", blend_file_path, "--python", script_path])

        # Clean up the temporary script
        os.remove(script_path)
        
        # Rename the exported file
        if os.path.exists(temp_fbx_file_path):
            # if final_fbx_file_path already exists, delete it
            if os.path.exists(final_fbx_file_path):
                os.remove(final_fbx_file_path)
            os.rename(temp_fbx_file_path, final_fbx_file_path)
            print(f"Exported and renamed to: {final_fbx_file_path}")
        else:
            print(f"Failed to export: {file_name}")
            print(f"Expected path: {temp_fbx_file_path}")

print("Exporting completed.")
