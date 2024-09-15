import numpy as np
import matplotlib.pyplot as plt

# Read in obj file and
# Return an array of vertices and faces
# (Ignore normals and materials for now)
def load_obj_file(filename):
    verts = []
    faces = []
    
    file = open(filename)
    for line in file:
        if not len(line.strip()): 
            continue
        line_type = line.strip().split()[0]
        line_elements = line.strip().split()[1:]
        # Look for vertices and add to verts list
        if line_type == 'v':
            verts.append([float(le) for le in line_elements])
        # Look for faces and add to faces list
        elif line_type == 'f':
            faces.append([int(le.split('/')[0]) for le in line_elements])
    return verts, faces

# Render the 3d object from an orthographic viewpoint
# Returns a rendered image
def draw_axes_in_image(image, axis, height, width, origin_h, origin_v):
    # Axes colours
    if axis == 'z':
        h_colour = [0.5, 0.0, 0.0]
        v_colour = [0.0, 0.4, 0.0]
    elif axis == 'y':
        h_colour = [0.5, 0.0, 0.0]
        v_colour = [0.0, 0.0, 0.5]
    elif axis == 'x':
        h_colour = [0.0, 0.0, 0.5]
        v_colour = [0.0, 0.4, 0.0]
    
    # Check if pixel is in visible area
    pixel_visible = lambda x, y: (x > 0) and (x < width) and (y > 0) and (y < height)
    
    # Draw axes
    for x in range(width):
        if pixel_visible(x, height-origin_v):
            image[height-origin_v-1, x, : ] = h_colour
    for y in range(height):
        if pixel_visible(origin_h, y):
            image[height-y-1, origin_h, : ] = v_colour

# Display the image in a noteboook
def show_image(image_in, size=10):
    fix, ax = plt.subplots(figsize=(size,size))
    plt.style.use('dark_background')
    plt.axis('off')
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    ax.imshow(image_in)