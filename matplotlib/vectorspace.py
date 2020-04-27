import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d(0, 5)
ax.set_ylim3d(0, 5)
ax.set_zlim3d(0, 5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# ax.quiver(0, 0, 0, 1, 1, 1, length = 0.5, normalize = True)
ax.quiver(0, 0, 0, 1, 2, 0, length=0.5)
ax.quiver(0, 1, 0, 1, 2, 0, normalize=True)
ax.quiver(0, 2, 0, 1, 2, 0)

plt.show()