import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,10,0.2)
def investy(n,t):
    dndt = -k*n*t
    return dndt

k = 0.1

n_0 = 100

invest = odeint(investy, n_0, t)
plt.plot(t, invest, label = 'инвестиция')
plt.title('инвестиция')
plt.xlabel('время')
plt.ylabel('деньги')
plt.show()
