############################################
############## Steven Walton ###############
######### walton.stevenj@gmail.com #########
### Python solutions to PS 232 Fall 2014 ###
############################################

# In the following code we will be using the numpy, math, and matplotlib
# modules for python2.7.  For efficiency we will only load the specific 
# functions from the functions that we need.


### Problem 1 ###
# For problem 1 we are asked to generate 1000 randomly generated points then plot them.  For part 1 we will be doing this in Cartesian coordinates, and in part 2 we will do this in polar coordinates.

## Part 1
# First thing we need to do is import the modules that we will be using for
# the first part of problem 1

# Much of this code will be similar to MatLab since numpy is similar to MatLab
from numpy import random as ran # random module will be called with ran
import matplotlib.pyplot as plt # plot will be called with plt

mu = 5                     # mu value for normal distribution
sigma = 1                  # standard deviation 
N=1000                     # number of coordinates we are creating
x = ran.normal(mu,sigma,N) # random numbers created with normal distribution 
y=1+4*ran.random(N)        # random numbers created between 1 and 5

# Plot is almost exactly the same as MatLab's version of plot
f = plt.plot(x,y,'.')      # plot the x and y coordinates with . as a marker
plt.show(f)                # show the plot that is generated from above



## Part 2
# We are asked to plot random points in polar coordinates 
from math import pi        # We need pi for our next plot
theta = 2 * pi * ran.random(N)   # randomly generated theta value, between 0 and 2pi
r = ran.random(N)          # random number generated between 0 and 1
p = plt.polar(theta,r,'r.')# polar plot in red
plt.show(p)                # shows the plot





## Problem 3 ##
# Now we are asked to plot a parametric curve.  The equation is given for x
# and y as below.  Variables are chosen for consistency and easy understanding
from numpy import arange   # arange creates a list from the first to the second with specified step sizes
from math import cos       # import cosine function
from math import sin       # import sine function
# Given variables
a = 2                      
b = 1
h = 1
step = .01
# We must create empty arrays that will be updated by loop
x3 = []
y3 = []
# We need to create an array in step sizes.  Step can be changed for accuracy 
phi = arange(0, 2*pi,step)

# We must use loops to append the arrays.  We will use a for loop and keep
# it in the range of phi, so that when step size changes the code does not
# break.
i = 0    # initialize i to be zero, regardless of previously stored value
for i in range(0, len(phi)):  
   x3.append((a + b) * cos(phi[i]) - h * cos(((a + b)/b) * phi[i]))

i = 0    # reinitialization of i
for i in range(0, len(phi)):
   y3.append((a + b) * sin(phi[i]) - h * sin(((a + b)/b) * phi[i]))

q = plt.plot(x3,y3,'g.')   # plot the function
plt.show(q)                # show the function

# For the rest of the problem we need to change values for a, b, h, and the
# range of phi.  This can easily be done with the above code and is left
# out of the solution.
