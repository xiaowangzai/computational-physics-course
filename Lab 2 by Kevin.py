# PHYS 3142 Lab2 Suggested solution by KWOK King Wai, Kevin

from numpy import linspace
from math import exp
from pylab import plot,show,xlabel,ylabel,title
from gaussxw import gaussxw
from adaptive import adapttrape,adaptsimp


print("==================== part 1a - Adaptive Methods ====================")

def f(x):
    return exp(-x*x)

print("Using adaptive trapezoidal rules:")
adapttrape(f,10,0,1,1.e-6,1.)
print("the number of sampling points needed to achieve the accuracy e-6 is 320")

print()

print("Using adaptive Simpson's rule:")
adaptsimp(f,10,0,1,1.e-6,1.)
print("the number of sampling points needed to achieve the accuracy e-6 is 20")

print()
print()
print("==================== part 1b - Trapezoidal Plot ====================")

xpoints=[]
ypoints=[]

for x in linspace(0,3,31):
    xpoints.append(x)
    ypoints.append(adapttrape(f,10,0,x,1.e-6,-1.))
title("$E(x)$ versus $x$")
ylabel("$E(x)$")
xlabel("$x$")
plot(xpoints,ypoints)
show()



print()
print()
print("==================== part 2b ====================")

V = 1.e-3
rho = 6.022e28
kB = 1.38e-23
theta = 428

def cv_trapezoidal(T):
    def g(x):
        if x == 0:
            return 0
        else:
            return 9*V*rho*kB*pow(T/theta,3)*pow(x,4)*exp(x)*pow(exp(x)-1,-2)

    return adapttrape(g,10,0,theta/T,1.e-6,1.)

print("For T = 500K:")
cv_trapezoidal(500)
print("the number of sampling points needed to achieve the accuracy e-6 is 40960")

print()

print("For T = 5K:")
cv_trapezoidal(5)
print("the number of sampling points needed to achieve the accuracy e-6 is 80")

print()
print()
print("==================== part 2c ====================")


def cv_gaussian(N,T,accuracy,pnt):
    def g(x):
        if x == 0:
            return 0
        else:
            return 9*V*rho*kB*pow(T/theta,3)*pow(x,4)*exp(x)*pow(exp(x)-1,-2)

    step = N
    a = 0
    b = theta/T
    gauss_sum_old = 0.
    error = 1

    while (error>accuracy):
        x,w = gaussxw(step)
        xp = 0.5*(b-a)*x+0.5*(b+a)
        wp = 0.5*(b-a)*w

        gauss_sum = 0.

        for k in range(step):
            gauss_sum += wp[k]*g(xp[k])

        error = abs(gauss_sum - gauss_sum_old)
        if(pnt > 0):
            if(step == N):
                print(step, gauss_sum)
            else:
                print (step, gauss_sum, error)
        gauss_sum_old = gauss_sum
        step += 1

    return gauss_sum

print("Using Gaussian quadrature:")
cv_gaussian(50,500,1.e-6,1.)
print("the number of sampling points needed to achieve the accuracy e-6 when T =500 K is 51")

print()

print("Using Gaussian quadrature:")
cv_gaussian(50,5,1.e-6,1.)
print("the number of sampling points needed to achieve the accuracy e-6 when T =5 K is 51")

upoints=[]
vpoints=[]

for u in linspace(5,500,496):
    upoints.append(u)
    vpoints.append(cv_gaussian(50,u,1.e-6,-1.))
title("$C_V(T)$ versus $T$")
ylabel("$C_V(T)$")
xlabel("$T$")
plot(upoints,vpoints)
show()