SCENE = ['chess', 'heads', 'fire', 'office', 'pumpkin', 'redkitchen', 'stairs']

import numpy as np

def process_large_point_cloud(file_path, comment='#'):
    # Initialize min and max values to None
    min_x, max_x = None, None
    min_y, max_y = None, None
    min_z, max_z = None, None
    min_error, max_error = None, None

    with open(file_path, 'r') as f:
        for line in f:
            # Skip comment lines
            if line.startswith(comment) or not line.strip():
                continue

            # Split the line into columns
            data = line.strip().split()
            
            # Extract X, Y, Z, and error values (assuming structure: POINT_ID X Y Z R G B ERROR)
            try:
                x, y, z, error = float(data[1]), float(data[2]), float(data[3]), float(data[7])
            except (IndexError, ValueError):
                print(f"Skipping invalid line: {line}")
                continue

            # Update min and max values for each coordinate and error
            min_x = x if min_x is None else min(min_x, x)
            max_x = x if max_x is None else max(max_x, x)
            min_y = y if min_y is None else min(min_y, y)
            max_y = y if max_y is None else max(max_y, y)
            min_z = z if min_z is None else min(min_z, z)
            max_z = z if max_z is None else max(max_z, z)
            min_error = error if min_error is None else min(min_error, error)
            max_error = error if max_error is None else max(max_error, error)

    # Print results after processing all rows
    print(f"Min X: {min_x}, Max X: {max_x}")
    print(f"Min Y: {min_y}, Max Y: {max_y}")
    print(f"Min Z: {min_z}, Max Z: {max_z}")
    print(f"Min Error: {min_error}, Max Error: {max_error}")

# Usage example
for sc in SCENE:
    print('Status of ' + sc + ' Scene')
    process_large_point_cloud('/workspace/7Scenes/' + sc + '/sfm_sift/points3D.txt')