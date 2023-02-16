import numpy as np
import matplotlib.pyplot as plt
from transformations import rotation_z, rotation_y, rotation_x
from figures import show_segments

class Polyedrom:
    def __init__(self, init_points, end_points):
        """init_p, end_p are np.ndarray's"""
        self.init_points = init_points
        self.end_points = end_points
    def __str__(self):
        return str(self.init_points) + str(self.end_points)
    def showPolyedrom(self, **kwargs):
        ax = plt.gca()
        show_segments(self.init_points, self.end_points, **kwargs)
    def rotationZ(self, theta):
        ax = plt.gca()
        rotated_init_points = self.init_points @ rotation_z(theta)
        rotated_end_points = self.end_points @ rotation_z(theta)
        return Polyedrom(rotated_init_points, rotated_end_points)
    def rotationY(self, theta):
        ax = plt.gca()
        rotated_init_points = self.init_points @ rotation_y(theta)
        rotated_end_points = self.end_points @ rotation_y(theta)
        return Polyedrom(rotated_init_points, rotated_end_points)
    def rotationX(self, theta):
        ax = plt.gca()
        rotated_init_points = self.init_points @ rotation_x(theta)
        rotated_end_points = self.end_points @ rotation_x(theta)
        return Polyedrom(rotated_init_points, rotated_end_points)
    def projectedByMatrix(self, matrix):
        projected_init_points = self.init_points @ matrix
        projected_end_points = self.end_points @ matrix
        return Polyedrom(projected_init_points, projected_end_points)
    def reflectedByMatrix(self, matrix):
        reflected_init_points = self.init_points @ matrix
        reflected_end_points = self.end_points @ matrix
        return Polyedrom(reflected_init_points, reflected_end_points)
    def traslatedByVector(self, vector):
        traslated_init_points = self.init_points + vector
        traslated_end_points = self.end_points + vector
        return Polyedrom(traslated_init_points, traslated_end_points)