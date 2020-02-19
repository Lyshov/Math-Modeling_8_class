from matplotlib import pyplot as plt 
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation 

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 100
a = np.linspace(0,10,N)

x = np.cos(a)
y = np.sin(a)
z = a

ball, = ax.plot(x,y,z,'o', color = 'g')
line, = ax.plot (x,y,z, '-', color = 'g')

def animatioonn(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])
    
ax.set_xlim3d([-1.0,1.0])
ax.set_xlabel('x')

ax.set_ylim3d([-1.0,1.0])
ax.set_ylabel('y')

ax.set_zlim3d([-1.0,1.0])
ax.set_zlabel('z')


ani = animation.FuncAnimation(fig,animatioonn,N, interval = 100)
ani.save('asdafs.gif')

