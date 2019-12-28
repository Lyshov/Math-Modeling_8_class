import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.01)
def dif_func(z, t):
    s, v= z
    dsdt=v
    dvdt=-g*np.sin(s/l)
    return dsdt, dvdt
l = 3
g = 10
s0 = 0
v0 = 4
z0 = s0,v0
solve = odeint(dif_func, z0, t)
plt.plot(t, solve)
plt.show()