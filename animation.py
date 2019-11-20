import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
R = 2
t=np.arange(-2*np.pi, 2*np.pi,0.1) 
fig, ax= plt.supplots()
ball, = plt.plot([], [], markers="o", color="r")
xdata, ydata = [],[]
ax.set_xlim(-2, 4*np.pi)
ax.set_ylim(-2, 2)
def update(t):
    ydata.append(np.sin(t))
    xdata.append(np.sin(t))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(-2*np.pi, 2*np.pi,0.1),interval = 50)
ani.save("animacha.gif")