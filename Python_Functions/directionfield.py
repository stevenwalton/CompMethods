#!/usr/bin/python
# Filename: directionfield.py

# Remember to either import * or import directionfield from this program
from numpy import *
from pylab import quiver
import matplotlib.pyplot as plt
from funcollection import *

def directionfield(funcname,xlims,ylims,n):
    x,y = meshgrid(linspace(xlims[0],xlims[1],n),linspace(ylims[0],ylims[1],n)) 
    v = zeros([n,n]); u = zeros([n,n])
    
    #u = cos(x); v = sin(y)
    for i in range(0, n):
        for j in range(0, n):
            dx = eval(funcname + '([x[i][j],y[i][j]], 0)')
            u[i,j] = dx[0]
            v[i,j] = dx[1]

    M = sqrt(pow(u, 2) + pow(v, 2))
    M[M==0] = spacing(1.)
    U = u/M; V=v/M;
    Q=quiver( x, y, U, V,units='x', pivot='mid', width=0.2,)
    
    plt.show()
    return x,y,u,v,Q

version = '0.1'

# End of directionfield.py
