import numpy as np
from polyhedron import Polyedrom

e1, e2, e3 = np.eye(3)[0], np.eye(3)[1], np.eye(3)[2]
origin = np.zeros_like(e1)
square_xy = np.vstack([origin, e1, e1+e2, e2])
square_xz = np.vstack([origin, e1, e1+e3, e3])
square_yz = np.vstack([origin, e2, e2+e3, e3])
square_xy_traslated = square_xy + e3
square_xz_traslated = square_xz + e2
square_yz_traslated = square_yz + e1
init_points = np.vstack([square_xy, square_xz, square_yz])
end_points = np.vstack([square_xy_traslated, square_xz_traslated, square_yz_traslated])
cube = Polyedrom(init_points, end_points)
cube = cube.traslatedByVector([2, 0, 0])
