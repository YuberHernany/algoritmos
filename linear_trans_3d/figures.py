import numpy as np
import matplotlib.pyplot as plt

def scenario_with_ticks():
    ax = plt.gca()
    ax.grid(False)
    ax.xaxis.pane.fill=False
    ax.yaxis.pane.fill=False
    ax.zaxis.pane.fill=False

def scenario_without_ticks():
    ax = plt.gca()
    ax.grid(False)
    ax.xaxis.pane.fill=False
    ax.yaxis.pane.fill=False
    ax.zaxis.pane.fill=False
    ax.set(xticks=(), yticks=(),zticks=(),)

def show_poits(points, **kwargs):
    ax = plt.gca()
    num_rows, num_cols = points.shape[0], points.shape[1]
    if num_cols == 3:
        ax.scatter(points[:,0], points[:,1], points[:,2], **kwargs)
    elif num_cols == 2:
        ax.scatter(points[:,0], points[:,1], **kwargs)

def show_paths(points, **kwargs):
    ax = plt.gca()
    num_rows, num_cols = points.shape[0], points.shape[1]
    if num_cols == 3:
        ax.plot(points[:,0], points[:,1], points[:,2], **kwargs)
    elif num_cols == 2:
        ax.plot(points[:,0], points[:,1], **kwargs)

def show_segments(points_init, points_end, **kwargs):
    ax = plt.gca()
    num_rows, num_cols = points_init.shape[0], points_init.shape[1]
    if num_cols == 3:
        for p_init, p_end in zip(points_init, points_end):
            seg = np.vstack([p_init, p_end])
            ax.plot(seg[:,0], seg[:,1], seg[:,2], **kwargs)
    elif num_cols == 2:
        for p_init, p_end in zip(points_init, points_end):
            seg = np.vstack([p_init, p_end])
            ax.plot(seg[:,0], seg[:,1], **kwargs)

def show_plane(w_normal, limits, **kwargs):
    """w_normal is like (a, b, c, d) coefs of equation ax+by+cz+d=0
    limits: iterable like (x_min, x_max, y_min, y_max)"""
    ax = plt.gca()
    x_min, x_max, y_min, y_max = limits
    a, b, c, d = w_normal
    X, Y = np.meshgrid([x_min, x_max], [y_min, y_max])
    Z = -(d/c) -(a/c)*X -(b/c)*Y
    ax.plot_surface(X, Y, Z, **kwargs)

def show_axis():
    plt.plot([0,0],[0,0],[-3,3], color='gray')
    plt.plot([0,0],[-3,3],[0,0], color='gray')
    plt.plot([-3,3],[0,0],[0,0], color='gray')