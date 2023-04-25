import math
from operator import add
def STR(a,b,c,N):
    a = a or 0
    b = b or 0
    c = c or 0
    try:
        sfr = (a + b + c) / N
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
    x = x or 0
    y = y or 0
    z = z or 0
    try:
        cri = (2.25*((2*x)+y+(0.5)*z)) / N
        cri = min(cri, 1.0)
        value52 = 20*cri
        return float(value52)
    except ZeroDivisionError:
        pass


def FQ(p1,p2,N):
    p1 = p1 or 0
    p2 = p2 or 0
    try:
        fqi = ((10*p1) +(6*p2)) / N
        value53 = 3 * fqi
        return float(value53)
    except ZeroDivisionError:
        pass


def FR(exp, N):
    if exp is None:
        exp = []
    x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0

    for i in range(len(exp)):
        x = exp[i]
        if x is not None:
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

    try:
        rpi = x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5
        value54 = 3 * (rpi / N)
        return float(value54)
    except ZeroDivisionError:
        pass


def FP(ow,tw,N):
    ow = [i * 5 if i else 0 for i in ow]
    tw = [i * 5 if i else 0 for i in tw]
    ad =  list(map(add,ow,tw))
    sm = []
    for i in ad:
        if i<=5:
            sm.append(i)
        elif i>5:
            sm.append(5)
    
    try:
        FPS=sum(sm)/N
        value55 = 3 * FPS
        return float(value55)
    except ZeroDivisionError:
        pass


def IWO(i1,N):
    i1= [i for i in i1 if i is not None]
    try:
        iws = sum(i1)/N
        value56 = 2.0 * iws
        return float(value56)
    except ZeroDivisionError:
        pass
