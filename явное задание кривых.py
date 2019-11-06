import matplotlib.pyplot as plt
import numpy as np
def parabola_and_giperbola(a=1,b=1,c=0,title="parabola_and_giperbola"):
    x=np.arange(0.01,10,0.02) 
    y1=a*x**2+b*x+c
    y2=a/x
    plt.plot(x,y1,y2,label="my parabola")
    plt.show()

parabola_and_giperbola()
