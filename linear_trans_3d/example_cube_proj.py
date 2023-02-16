import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.animation as animation
from figures import scenario_without_ticks
from figures import show_axis, show_plane
from polyhedron import Polyedrom    
from transformations import projection_matriz
from cube_example import cube

v1 = np.array([1, 0, -1]).reshape(-1, 3)
v2 = np.array([0, 1, -1]).reshape(-1, 3)
v3 = np.cross(v1, v2)
points = np.vstack([v1, v2])
P = projection_matriz(v1, v2)

plt.style.use("dark_background")
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
thetas = np.linspace(0, 2 * np.pi, 100)
scenario_without_ticks()
ax.axis("off")

cubes_rotatedx = [cube.rotationX(theta) for theta in thetas]

cubes_projected = [rcube.projectedByMatrix(P) for rcube in cubes_rotatedx]

line, = plt.plot([],[],[])


def update(i):
    ax = plt.gca()
    ax.cla()
    ax.set(xlim=(-3,3),ylim=(-3,3), zlim=(-3,3))
    plt.plot([0,0],[0,0],[-3,3], color='yellow')
    show_plane([1,1,1,0], [-3,3,-3,3], alpha=0.6, color='gray')
    scenario_without_ticks()
    show_axis()
    cubes_rotatedx[i].showPolyedrom(color='red')
    cubes_projected[i].showPolyedrom(color='gray')
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=10)
ani.save('projection_cube.gif')