import numpy as np
def funcsiy(a):
    s = 1
    for i in range(0,len(a),1):
        s = s*a[i]
    print(s)
    
a = np.arange(1,10,2)
funcsiy(a)
    