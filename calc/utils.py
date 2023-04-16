
def STR(a,b,c,N):
    sfr = (a + b + c) / N
    try:
        value51 = 20 * (20/sfr)
        if value51 <= 15:
            return 20
        elif value51 <= 17:
            return 18
        elif value51 <= 19:
            return 16
        elif value51 <= 21:
            return 14
        elif value51 <= 23:
            return 12
        elif value51 <= 25:
            return 10
        else:
            return 0
    except ZeroDivisionError:
        pass

def FCR(x,y,z,N):
    cri = (2.25*((2*x)+y+(0.5)*z)) / N
    cri = min(cri, 1.0)
    value52 = 20*cri
    return value52

def FQ(p1,p2,N):
    fqi = ((10*p1) +(6*p2)) / N
    value53 = 3 * fqi
    return value53

def FR(exp,N):
    x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0

    for i in range(len(exp)):
        x = exp[i]
        if x == 1:
            x1 += 1
        elif x == 2:
            x2 += 1
        elif x == 3:
            x3 += 1
        elif x == 4:
            x4 += 1
        elif x >= 5:
            x5 += 1
        else:
            pass

    rpi = x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5
    value54 = 3 * (rpi / N)
    return value54

def Fp(tw,ow,N):
    value55 = tw
    return value55