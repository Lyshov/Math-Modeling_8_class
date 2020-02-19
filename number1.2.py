import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

t = np.arange(0.01, 4*np.pi,0.01)

p = np.linspace(-2*np.pi,2*np.pi,100)
t = np.linspace(-2*np.pi,2*np.pi, 100)

a = 1
b = 2
c = 3

x= a *np.outer(np.cos(p),np.sinh(t))
y= b * np.outer(np.sin(p),np.sinh(t))
z= c *  np.outer(np.ones(np.size(p)),np.sinh(t))

ax.plot_surface(x,y,z, color = 'b')

plt.show()
