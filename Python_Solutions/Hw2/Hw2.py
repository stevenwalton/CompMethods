###############################################################
###############################################################
#########################  Steven Walton  #####################
##################### walton.stevenj@gmail.com ################
###############################################################
###############################################################

##### Problem 1 #####

import numpy as np
from numpy import linalg as lin

print "Problem 1"

# First we need to initialize the arrays that we are going to use
a = np.array([[2,1,2],[3,2,1],[1,1,1]])
b = np.array([1,1,1])                   # Notice that this is a normal vector
                                        # numpy knows to transpose it
x = lin.solve(a,b)
print "(x,y,z) =",
print x


##### Problem 2 #####
print ""
print "Problem 2"


# For this we will be doing Taylor expansions.  Write it out by hand first.  
from math import factorial as fac       # saves us from writing math.factorial() every time
x = np.pi/3                             # This is a float

sinx = 0 + x - (x**3)/fac(3) + (x**5)/fac(5) - (x**7)/fac(7) + (x**9)/fac(9) - (x**11)/fac(11) + (x**13)/fac(13)
cosx = 1 - (x**2)/fac(2) + (x**4)/fac(4) - (x**6)/fac(6) + (x**8)/fac(8) - (x**10)/fac(10) + (x**12)/fac(12) - (x**14)/fac(14)

tanx = sinx/cosx
print "tan(pi/3) is about ",
print tanx

# To make sure that we have it to 10 decimal places we'll check from the value that wolfram gives us
real = 1.7320508075688772935274463415058723669428052538103806
diff = real - tanx
# I'll introduce a single line if then else statement
# notice where the print statement is
print "We're accurate to at least 10^-10" if diff < 10**-10 else  "Not accurate enough"



##### Problem 3 #####
# In this one we need to plot
from matplotlib import pyplot as plt
print ""
print "Problem 3"

# We want to find N primes (10000), in sequential order.  We use N so we can change it 
# to any arbitrary number and still have our code work

N       = 10000
primes  = np.zeros(N)  # This size will change with N
found   = 0                 # Initialize
num     = 0                 # What we'll be testing
i       = 0
# Here we will define our factoring function
# And we'll introduce how to define a function
def isPrime(n):
    return all(n% i for i in xrange(2,n))

while found < N:
    num += 1
    if isPrime(num) == True:
        found += 1
        primes[i] = int(num)
        i += 1
diff = np.zeros(N-1)
for z in range(0,N-1):
    diff[z] = int(primes[z+1]) - int(primes[z])

plt.xlabel('Distance between primes')
plt.ylabel('Number of occurrences')
# Note, we can use LaTex notation in labels and titles
# use pattern $\rho=100$
plt.title('Histogram of the difference between adjacent primes')
plt.hist(diff)
plt.show()

