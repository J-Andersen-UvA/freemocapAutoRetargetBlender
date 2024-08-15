import bpy
import sys
from pathlib import Path

# Set the path to the freemocap addon
freemocap_path = "freemocap_adapter"
sys.path.append(freemocap_path)

# Import the function if it's in a module
from freemocap_adapter.core_functions import apply_foot_locking  # Adjust the import according to the actual module structure

# Call the function with the correct parameters
apply_foot_locking(
    # target_foot=['left_foot', 'right_foot'],
    target_foot=['left_foot', 'right_foot'],
    target_base_markers=['foot_index', 'heel'],
    z_threshold=0.01,
    ground_level=0.0,
    frame_window_min_size=10,
    initial_attenuation_count=5,
    final_attenuation_count=5,
    lock_xy_at_ground_level=True,
    knee_hip_compensation_coefficient=0.25,
    compensate_upper_body=True
)
