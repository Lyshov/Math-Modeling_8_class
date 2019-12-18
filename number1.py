import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,100,0.1)
def razmnozhenie_bacteriy(n,t):
    dndt = k*n
    return dndt

k = 0.05

n_0 = 1

razmo = odeint(razmnozhenie_bacteriy, n_0, t)
plt.plot(t, razmo, label = 'кол-во бактерий')
plt.title('кол-во бактерий')
plt.show()
    