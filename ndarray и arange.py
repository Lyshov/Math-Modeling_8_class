import numpy as пр
from constant import g
y0 = 3
x0 = 1
v0x= 2
t = пр.arange(0,5,0.01)
N = len(t)
coord_and_vel=пр.ndarray(shape = (N,3))
for i in range(0,N,1):
    x = x0+v0x*t[i]
    y = y0+v0x*t[i]-((g*t[i]**2)/2)
    coord_and_vel[i,0]=t[i]
    coord_and_vel[i,1]=x
    coord_and_vel[i,2]=y
print(coord_and_vel)    


