import numpy as np
import matplotlib.pyplot as  plt
import matplotlib.animation as animation
from figures import scenario_without_ticks
from figures import show_axis, show_plane
from polyhedron import Polyedrom    
from transformations import projection_matriz
from cube_example import cube


plt.style.use("dark_background")
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
thetas = np.linspace(0, 2 * np.pi, 100)
scenario_without_ticks()
ax.axis("off")


cubes_rotatedx = [cube.rotationX(theta) for theta in thetas]
cubes_rotatedy = [cube.rotationY(theta) for theta in thetas]
cubes_rotatedz = [cube.rotationZ(theta) for theta in thetas]

line, = plt.plot([],[],[])

def update(i):
    ax = plt.gca()
    ax.cla()
    ax.set(xlim=(-3,3),ylim=(-3,3), zlim=(-3,3))
    plt.plot([0,0],[0,0],[-3,3], color='yellow')
    scenario_without_ticks()
    show_axis()
    cubes_rotatedx[i].showPolyedrom(color='red')
    cubes_rotatedy[i].showPolyedrom(color='green')
    cubes_rotatedz[i].showPolyedrom(color='yellow')
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=10)
ani.save('rota.gif')

