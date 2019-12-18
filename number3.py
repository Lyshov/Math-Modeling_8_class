import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0,10,0.1)

m = 15

def scorost(v,t):
    dvdt = (F-k*v**2)/m
    return dvdt
k = 0.07
v_0 = 0
F =  150
zakon_izm_scorosti = odeint(scorost, v_0, t)
plt.plot(t, zakon_izm_scorosti, label = 'бег в воде')
plt.title('бег в воде')
plt.xlabel('t')
plt.ylabel('скорость')
plt.show()
