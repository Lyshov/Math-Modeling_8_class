import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

second_in_year=365*24*60*60
second_in_day=24*60*60
year = 1
t = np.arange(0, year * second_in_year,second_in_day)
def grav_func(z,t):
    
    (x_earth, v_x_earth, y_earth, v_y_earth,
     x_merc, v_x_merc,y_merc,v_y_merc) = z
     
    dxdt_earth=v_x_earth
    dv_xdt_earth=- G * sun_mass*x_earth/(x_earth**2+y_earth**2)**1.5
    dydt_earth=v_y_earth
    dv_ydt_earth=- G * sun_mass*y_earth/(x_earth**2+y_earth**2)**1.5
     
    dxdt_merc=v_x_merc
    dv_xdt_merc =- G * sun_mass*x_merc/(x_merc**2+ y_merc **2)**1.5
    dydt_merc=v_y_merc
    dv_ydt_merc =- G * sun_mass*y_merc/(x_merc**2+y_merc**2)**1.5
    
    return (dxdt_earth,dv_xdt_earth,dydt_earth,dv_ydt_earth,
            dxdt_merc,dv_xdt_merc,dydt_merc,dv_ydt_merc)

x0_earth = 0
v_x0_earth = 30000
y0_earth= -149*10**9
v_y0_earth = 0

x0_merc= 57909227000
v_x0_merc=0
y0_merc=0
v_y0_merc=47360

z0=(x0_earth,v_x0_earth,y0_earth,v_y0_earth,
    x0_merc,v_x0_merc,y0_merc,v_y0_merc)

G = 6.67*10**(-11)
sun_mass=1.9*10**30

sol = odeint(grav_func, z0, t)

fig = plt.figure()
planets = []

for i in range (0, len(t),1):
    sun, = plt.plot([0],[0],'yo',ms = 10)
    
    earth, = plt.plot(sol[:i,0],sol[:i,2], 'g-')
    earth_line,=plt.plot(sol[i,0],sol[i,2], 'go')
    
    merc, = plt.plot(sol[:i,4],sol[:i,6], 'r-')
    merc_line,=plt.plot(sol[i,4],sol[i,6], 'ro')
    
    planets.append([sun,earth,earth_line,merc,merc_line])

ani = ArtistAnimation(fig, planets, interval = 1)
plt.axis('equal')
ani.save('earth_merc.gif')
