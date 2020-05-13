import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d(0, 3)
ax.set_ylim3d(0, 3)
ax.set_zlim3d(0, 3)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# ax.quiver(x, y ,z, x, y, z) first 3 param are origin definition, following 3 are vector definition


# ax.quiver(0, 0, 0, 1, 1, 1, length = 0.5, normalize = True)
# ax.quiver(0, 0, 0, 1, 2, 0, length=0.5)
# ax.quiver(0, 1, 0, 1, 2, 0)
# ax.quiver(0, 2, 0, 1, 2, 0)

ax.quiver(0, 0, 0, 1,-1,1)
ax.quiver(0, 0, 0, 0, 1, -1)
ax.quiver(0, 0, 0, -1, 0, 1)

plt.show()