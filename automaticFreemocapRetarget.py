import subprocess
import os
import sys
import argparse

# Define the function to process each Blender file
def process_blend_file(blender_path, blender_file, scripts):
    print(f"Processing Blender file: {blender_file}")
    # Construct the full command to open Blender and run all scripts
    command = [blender_path, blender_file]
    if not "--foreground" in sys.argv:
        command.append("--background")
    for script in scripts:
        command.extend(["--python", script])
    
    # Print the command for debugging purposes
    print(f"Running command: {' '.join(command)}")

    # Use Popen for real-time output
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        while True:
            output = process.stdout.readline()
            if output:
                print(output.strip())
            else:
                break
        stderr_output = process.stderr.read()
        if stderr_output:
            print(stderr_output.strip())

        process.wait()

        if process.returncode != 0:
            print(f"Error processing {blender_file}")
        else:
            print(f"Finished processing: {blender_file}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Run Blender scripts on multiple Blender files.")
    parser.add_argument("--folder", type=str, help="Path to the folder containing Blender files.", required=True)
    parser.add_argument("--foreground", action="store_true", help="Option to run Blender in the foreground instead of background.")
    parser.add_argument("--autoScale", action="store_true", help="Option to autoScale the RPM avatar to match the source armature scale.")
    args = parser.parse_args()

    # Path to the Blender executable
    blender_path = "C:/Program Files/Blender Foundation/Blender 4.0/blender.exe"

    # Paths to the scripts
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, "blenderScripts")
    scripts = [
        os.path.join(script_dir, "freemocapAddRig.py"),
        # os.path.join(script_dir, "importGlassesGuyFBX.py"),
        os.path.join(script_dir, "importGlassesGuyGLTF.py"),
    ]
    
    if args.autoScale:
        print("Auto-scaling RPM avatars.", flush=True)
        scripts.append(os.path.join(script_dir, "autoScaleRPM.py"))
    
    scripts.extend([
        os.path.join(script_dir, "selectArmaturesPoseMode.py"),
        os.path.join(script_dir, "expyKitBind.py"),
        # os.path.join(script_dir, "expykitBakeAnimByName.py"),
        os.path.join(script_dir, "assignAnimDataSelectActionByName.py"),
        # os.path.join(script_dir, "bakeAndAssignAnim.py"),
        # os.path.join(script_dir, "unscaleRPM.py"),
        # os.path.join(script_dir, "restoreBoneRolls.py"),
        os.path.join(script_dir, "exportGLTFGG.py"),
        # os.path.join(script_dir, "exportFBXGG.py"),
        # os.path.join(script_dir, "blenderQuit.py")
    ])

    # Get all .blend files in the specified folder
    blend_files = [os.path.join(args.folder, f) for f in os.listdir(args.folder) if f.endswith('.blend')]

    if not blend_files:
        print("No Blender files found in the specified folder.")
        sys.exit(1)

    # Process each Blender file
    for blend_file in blend_files:
        process_blend_file(blender_path, blend_file, scripts)

if __name__ == "__main__":
    main()
