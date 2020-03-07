import numpy as np
from scipy.integrate import odeint 
import matplotlin.pyplot as plt 
from matplotlib.animation import ArtistAnimation

s_y=365*24*60*60
s_d=24*60*60
y= 2
t = np.arange(0, y*s_y, s_d)

def move_func(s,t):
    (x1,v_x1,y1,v_y1,
    x2,v_x2,y2,v_y2,
    x3,v_x3,y3,v_y3,
    x4,v_x4,y4,v_y4) = s
    
    dxdt1 =v_x1
    dv_xdt1 = (-G*m2*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
            -G*m3*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5)
    
    dydt1 =v_y1
    dv_ydt1 = (-G*m2*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
            -G*m2*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5)
   
    
    dxdt2 =v_x2
    dv_xdt2 = (-G*m1*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
            -G*m3*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    dydt2 =v_y2
    dv_ydt2 = (-G*m1*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
            -G*m3*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5)
    
    
    dxdt3 =v_x3
    dv_xdt3 = (-G*m1*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
            -G*m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    
    dydt3 =v_y3
    dv_ydt3 = (-G*m1*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
            -G*m2*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5)
    
    dxdt4 = v_x4
    dv_xdt4 = (-G*m1*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
            -G*m3*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5)
    
    dydt4 = v_y4
    dv_ydt4 = (-G*m1*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
            -G*m3*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5)
    
    return (dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4)
    