import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0.01,100,0.1)
R = 5
x = R*(np.sin(t))**3
y = R*(np.cos(t))**3
z = np.cos(2*t)
ax.plot(x,y,z, label ='number3')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('afssgafwedfas')
plt.show()