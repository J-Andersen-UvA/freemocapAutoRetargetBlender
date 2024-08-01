# FreeMoCap Blender Auto Retarget

**freemocapBlenderAutoRetarget** is a Python script for automating the process of retargeting animations and exporting FBX files in Blender. This script is designed to streamline animation workflows, particularly for integrating FreeMoCap rigs and animations.

## Features

- **Batch Processing**: Automatically processes multiple `.blend` files in a specified directory.
- **Script Automation**: Runs a series of predefined Blender Python scripts for rigging, baking, and exporting animations.
- **Real-Time Output**: Provides real-time output during script execution for better monitoring and debugging.

## Prerequisites

- **Blender**: Ensure [Blender](https://www.blender.org/) is installed on your system. The script is configured for Blender 4.0.
- **Python**: Python 3.x is required. The script uses `subprocess` for running Blender commands.
- **FreeMoCap adapter Addon**: The script integrates with the [FreeMoCap adapter Blender addon by ajc-27](https://github.com/ajc27-git/freemocap_tools). Ensure the addon is installed and properly configured in Blender.
- **ExpyKit Addon**: The script also relies on the [ExpyKit addon by ballsandninjas](https://ballsandninjas.gumroad.com/l/xotibs) for animation retargeting.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/freemocapBlenderAutoRetarget.git
   cd freemocapBlenderAutoRetarget```
2. **Configure Blender Path**:
   - Edit the main() function in auto_retarget.py to set the path to your Blender executable (blender_path).

## Usage

1. **Prepare Your Blender Files**:
   - Place your `.blend` files in a directory.

2. **Change the avatar or keep the same**:
   - Change the avatar from glasses guy to another avatar. Make sure to pose align the avatar with the Freemocap avatar before running the script.
        - If the avatar has been changed alter the corresponding scripts to use your new avatar.

3. **Run the Script**:
   - Open a terminal and navigate to the project directory.
   - Run the script using the following command:
     ```bash
     python automaticFreemocapRetarget.py --folder /path/to/your/blend/files
     ```
   - Replace `/path/to/your/blend/files` with the path to your directory containing `.blend` files.

## Notes
Currently only tested for the glassesguy avatar made with [ReadyPlayerMe](https://readyplayer.me/)
