import numpy as np

# Set up the scene world coordinates
# Right handed coordinate system
# X - Right is positive direction
# Y - Up is positive direction
# Z - Positive direction is "out of the screen"
class SceneCoords():
    def __init__(self, x_0, x_1, y_0, y_1, z_0, z_1):
        self.x_0, self.x_1 = x_0, x_1
        self.y_0, self.y_1 = y_0, y_1
        self.z_0, self.z_1 = z_0, z_1
        self.axis = None
        
    # Set which axis the ortho render is based on
    def set_axis(self, axis):
        if axis == 'z':
            self.axis = 'z'
            self.h_ref, self.v_ref, self.d_ref = 0, 1, 2
            self.h_0, self.v_0 = self.x_0, self.y_0
        elif axis == 'y':
            self.axis = 'y'
            self.h_ref, self.v_ref, self.d_ref = 0, 2, 1
            self.h_0, self.v_0 = self.x_0, self.z_0
        elif axis == 'x':
            self.axis = 'x'
            self.h_ref, self.v_ref, self.d_ref = 2, 1, 0
            self.h_0, self.v_0 = self.z_0, self.y_0
        else:
            self.axis = None
    

    # Return horizontal length (based on axis)
    def h_len(self):
        if self.axis == 'z' or self.axis == 'y':
            length = self.x_1 - self.x_0
        elif self.axis == 'x':
            length = self.z_1 - self.z_0
        else:
            length = None
        return length

    # Return vertical length (based on axis)
    def v_len(self):
        if self.axis == 'z' or self.axis == 'x':
            length = self.y_1 - self.y_0
        elif self.axis == 'y':
            length = self.z_1 - self.z_0
        else:
            length = None
        return length

# Find the world coordinates to used from the model
def scene_coords_from_model(verts):
    verts_np = np.array(verts)
    x_0, y_0, z_0 = verts_np.min(axis=0)
    x_1, y_1, z_1 = verts_np.max(axis=0)
    return SceneCoords(x_0, x_1, y_0, y_1, z_0, z_1)