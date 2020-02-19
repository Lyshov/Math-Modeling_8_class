import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

t = np.arange(0.01, 4*np.pi,0.01)

p = np.linspace(0,2*np.pi,100)
t = np.linspace(0,2*np.pi, 100)

x= np.outer(p, np.cos(t))
y= np.outer(p, np.sin(t))
z= np.outer(p**2, np.ones(np.size(t)))

ax.plot_surface(x,y,z, color = 'g')

plt.show()
