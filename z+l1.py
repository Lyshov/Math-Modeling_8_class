import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation 

s_y=365*24*60*60
s_d=24*60*60
d = 5

t = np.arange(0,d*s_d, 60)

def move_func(s,t):
    (xz,v_xz,yz,v_yz,
    xl,v_xl,yl, v_yl)
    
    dxdt1=v_xz
    dv_xdt1 = -G*m_l*(xz-xl)/((xz-xl)**2+(yz-yl)**2)**1.5
    dydt1=v_yz
    dv_ydt1 = -G*m_l*(yz-yl)/((xz-xl)**2+(yz-yl)**2)**1.5
    
    dxdt2=v_xl
    dv_xdt2 = -G*m_z*(xl-xz)/((xl-xz)**2+(yl-yz)**2)**1.5
    dydt2=v_yl
    dv_ydt2 = -G*m_z*(yl-yz)/((xl-xz)**2+(yl-yz)**2)**1.5
    
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2)

r_z = 6371000
r_l = 1731100
 
xz=0
v_xz=0
yz=0
v_yz=0

xl=384401000
v_xl=0
yl=0
v_yl=0

s0= (xz,v_xz,yz,v_yz,
    xl,v_xl,yl,v_yl)

m_z = 5.97*10**24
m_l = 7.35*10**22
     
G = 6.67*10**(-11)

move_array = np.ndarray(shape=(len(t),4))
for i in range(1,len(t)-1,1):
    tau = [t[i], t[i+1]]
    
    sol = odeint(move_func, s0, tau)
    
    move_array[i,0] = sol[1,0]
    move_array[i,1] = sol[1,2]
    move_array[i,2] = sol[1,4]
    move_array[i,3] = sol[1,6]
    
    xz= sol[1,0]
    v_xz= sol[1,1]
    yz= sol[1,2]
    v_yz= sol[1,3]
    
    xl=sol[1,4]
    v_xl=sol[1,5]
    yl=sol[1,6]
    v_yl=sol[1,7]
    
    r12= np.sqrt((xz-xl)**2+(yz-yl)**2)
    
    if r12 <= (r_z+r_l):
        V_xz = (2*m_l*v_xl+v_xz*(m_z-m_l))/(m_z+m_l)
        V_xl = (2*m_z*v_xz+v_xl*(m_l-m_z))/(m_z+m_l)
    else:
        V_xz = v_xz
        V_xl = v_xl
    s0=(xz, V_xz,yz,v_yz,
        xl,V_xl,yl,v_yl)
    
fig = plt.figure()
bodys = []

for i in range (0, len(t)-1,1):
    body1, =plt.plot(move_array[i,0],move_array[i,1], 'o', color = 'g',ms = 6)
    body1_line, = plt.plot(move_array[:i,0],move_array[:i,1], '-', color = 'g')
    
    body2, =plt.plot(move_array[i,2],move_array[i,3], 'o', color = 'r',ms = 6)
    body2_line, = plt.plot(move_array[:i,2],move_array[:i,3], '-', color = 'r')
    
    bodys.append([body1,body1_line,body2,body2_line])
    
ani = ArtistAnimation(fig,bodys,interval = 1)
plt.axis('equal')
ani.save('z+l.gif')
