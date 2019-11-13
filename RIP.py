def RIP(m_ast,v_stolk):
    c = 4200
    m = 1400000000000000000000 
    t1 = 15
    k = m_ast*(v_stolk**2)/2
    t2 = k/c/m+t1
    t3 = t2-t1
    print(t3)
    if t3>50 and t3<100:
        print("МИНУС 90%")
    elif t3>30 and t3<50:
        print("ты не умрешь, но это не точно")
    else:
        print("все относительно не плохо")
RIP(10000000000000000000,2000000)

    