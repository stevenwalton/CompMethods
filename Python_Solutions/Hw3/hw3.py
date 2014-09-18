# We will only need these two modules for the entire homework (as usual)
import numpy as np
import matplotlib.pyplot as plt

### Problem 1 ###


N = 1200                    # resolution we will be using, note that
                            # this is so code is easily modifiable (style)
x = np.linspace(-10,10,N)
y = np.linspace(-10,10,N)

X, Y = np.meshgrid(x,y)     # We can define meshgrid this way

# Note the use of np.sin and np.arctan and not math.sin/math.atan
# The reason we do this is because numpy is able to handle arrays 
# better than the normal math package.  It will not work with the math
# package.  Trust me, I tried
F = np.sin(X*Y)
G = np.arctan(X/Y)

# We want to do a contour plot of the function
plt.contour(X,Y, (F-G),[0])
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(xy)-arctan(x/y)=0')
plt.show()

### Probelm 2 part b ###

# Params given by problem
a = 5*(10**(-3))
y0 = 1

# Step and scale (again, for modifiability)
h = 0.1
t = np.arange(0,600,h)

# Initialization
y = np.zeros(len(t))
y[0]=y0

# Solve using Euler's method
for i in range(1,len(t)):
   y[i] = y[i-1] - h*a*y[i-1]
   
# Analytical solution
yExact = y0*np.exp(-a*t)

# Note that x's and +'s have a black outline
plt.plot(t,y,'rx')
plt.plot(t,yExact,'b+')
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
# Calling plt.title as follows will show us current value of a
# We are coders, and we write with style/laziness 
plt.title('dy/dt=-ay, a = %f'%a)
plt.show()


### Problem 3 ###

# Given Parameters from problem
a = 5*(10**(-3))
b = 1*(10**(-5))
omega = 2 * np.pi/30
y0 = 1

# redefine t for new step size (though we could have kept t the same
# this is more about code style
h = 0.01
t = np.arange(0,600,h)

# We do need to reset y though (similar)
y = np.zeros(len(t))
y[0] = y0

# Euler's
# we could use the same indexing parameter, i, as above, but this is better
# practice and style.  We don't want to confuse ourselves/others
for n in range(1,len(t)):
   y[n] = y[n-1] - h*a*y[n-1] + b*np.cos(omega*t[n-1])

plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Height Of Rum In Barrel (m)')
plt.title('Rum Barrel With A Hole On A Ship')
plt.show()
