__author__ = 'greta9a1'

import numpy as n


def rabbitsandfoxes(x, t):
    a = 2.
    b = 0.1
    c = 0.5
    d = 0.02
    u = x[0]
    v = x[1]
    xdot = n.zeros(2)

    xdot[0] = a*u - b*v*u
    xdot[1] = -c*v + d*u*v
    
    return xdot
    
    
def humansandzombies(x, t)    :
    m = 0.05
    k = 0.33
    D = 2.
    h = x[0]
    z = x[1]
    xdot = n.zeros(2)

    xdot[0] = -k*m*h*z
    xdot[1] =  k*m*h*z - pow( (1.-k),(m*h*D) )*z/D

    return xdot