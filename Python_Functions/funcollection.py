# Collection of competition functions

# Remember to either import * (all) or import each definition individually from funcollection
__author__ = 'Dead Luck'

import numpy as n


def foxesandrabbits(x, t):
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


def humansandzombies(x, t):
    m = 0.05
    k = 0.33
    D = 2.
    h = x[0]
    z = x[1]
    xdot = n.zeros(2)

    xdot[0] = -k*m*h*z
    xdot[1] =  k*m*h*z - pow( (1.-k),(m*h*D) )*z/D

    return xdot

def competingarmies(x, t):
    alpha = 5.
    gamma = 7.
    beta = 1/2500.
    delta = 1/1500.
    eta = 0
    zeta = 0
    A = x[0]
    B = x[1]

    xdot = n.zeros(2)
    xdot[0] = alpha*A - beta*A*B - eta*B
    xdot[1] = gamma*B - delta*A*B - zeta*A
    return xdot

version = '0.2'
