#PHYS 3142 Lab 3 suggested solution part 1cii
#By Ng Ka Ho, Tony
from numpy import sin,sqrt
    
def f(x):
    if x!=0:
        return 1/sqrt(sin(x))-1/sqrt(x)
    else:
        return 0

def cv_trapezoidal(N):
    a = 0
    b = 1
    h = (b-a)/N
    s=(f(a)+f(b))/2.0
    for k in range(1,N):
        s += f(a+k*h)
    s *= h
    return s

def Ti(N):
    a = 0
    b = 1
    sum = 0.
    h = (b-a)/N
    for i in range(1,N,2):
        sum += f(a+i*h)
    sum*=h
    return sum

print("parts (1ci) and (1cii)- derivation see word file")
print("Program part -20 marks")
N=10
error=1
accuracy = 1e-8
trap_sum_old=cv_trapezoidal(N)
#print("N=",a,N,trap_sum_old)

while(error>accuracy):
    N*=2
    trap_sum = trap_sum_old/2. + Ti(N)
    error=1/3*abs(trap_sum-trap_sum_old)
    trap_sum_old=trap_sum

print("The result is",trap_sum+2)