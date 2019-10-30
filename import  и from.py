from constant import M,g,R,k,e,H
from math import pi,sqrt
print(pi)
print(sqrt)
h = 100 
v = sqrt(g*h*pi/(2*M*R)) 
print(v) 
T = 200 
E = 300
N = (2/sqrt(pi))*(H/(k*T)**1.5)*e**(-E/k*T)*E**(T/2)
print(N)