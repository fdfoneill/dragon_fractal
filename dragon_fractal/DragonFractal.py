import matplotlib.pyplot as plt
import numpy as np

class DragonFractal:
    def __init__(self, *vertices):
        if vertices is not None and len(vertices) != 0:
            self.vertices = np.array(vertices)
        else:
            self.vertices = np.array([0+0j, 64+0j])
    
#    @property
    def plot(self):
        plt.clf()
        x = [v.real for v in self.vertices]
        y = [v.imag for v in self.vertices]
        plt.plot(x, y)
        plt.show()
    
    def step(self, n_steps=None):
        if n_steps != None:
            for i in range(n_steps):
                self.step()
        else:
            first_step_old = self.vertices[1] - self.vertices[0]
            segment_length_old = np.sqrt((first_step_old.real**2) + (first_step_old.imag**2))
            segment_length_new = np.sqrt((segment_length_old**2)/2)
            segment_scaling_factor = segment_length_new / segment_length_old
            n_vertices_old = len(self.vertices)
            vertices_old = self.vertices.copy()
            vertices_new = np.empty(2*n_vertices_old - 1, dtype=vertices_old.dtype)
            vertices_new[0::2] = vertices_old
            for i in range(n_vertices_old - 1):
                existing_line = vertices_old[i+1] - vertices_old[i]
                # 1-based index of the element to the left is (i+1)
                if (i + 1) % 2 == 1:
                    extra_sauce = (existing_line * ((np.sqrt(2)/2)+(1j*np.sqrt(2)/2)) * segment_scaling_factor) # bend left
                else:
                    extra_sauce = (existing_line * ((np.sqrt(2)/2)-(+1j*np.sqrt(2)/2)) * segment_scaling_factor) # bend right
                vertices_new[2*i + 1] = vertices_old[i] + extra_sauce
            self.vertices = vertices_new