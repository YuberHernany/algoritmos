import numpy as np
import matplotlib.pyplot as plt

def rotation_z(theta):
    R_z = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta),  np.cos(theta), 0],
                    [0, 0, 1]])
    return R_z

def rotation_y(theta):
    R_y = np.array([[np.cos(theta), 0,  -np.sin(theta)],
                    [0,             1,              0],
                    [np.sin(theta), 0,  np.cos(theta)]])
    return R_y

def rotation_x(theta):
    R_x = np.array([[1,             0,          0],
                    [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta),  np.cos(theta)]])
    return R_x

def projection_matriz(v1, v2):
    A = np.hstack([v1.reshape(-1,1), v2.reshape(-1,1)]).reshape(-1, 2)
    return A @ np.linalg.inv(A.T @ A) @ (A.T)

def reflection_3d(P_matrix):
    """ INPUT: P_matrix (ndarray 2D representing projection over a plane)
    OUTPUT: H (ndarray 2D square representing reflection)"""
    H = 2 * P_matrix - np.eye(3)
    return H


