#PHYS 3142 Lab 3 suggested solution
#By Ng Ka Ho, Tony
from numpy import linspace,sin,sqrt,log,exp
from gaussxw import gaussxwab
from pylab import plot,ylim,show,xlabel,ylabel

def f(x):
    return 1/sqrt(sin(x))
    
def g(x):
    return 1/sqrt(sin(x))-1/sqrt(x)

def cv_trapezoidal(a,N):
    b = 1
    h = (b-a)/N
    s=(f(a)+f(b))/2.0
    for k in range(1,N):
        s += f(a+k*h)
    s *= h
    return s

def Si(a,N):
    b = 1
    sum =f(a)+f(b)
    h = (b-a)/N
    for i in range(2,N-1,2):
        sum += 2*f(a+i*h)
    sum*=h/3
    return sum

def Ti(a,N):
    b = 1
    sum = 0.
    h = (b-a)/N
    for i in range(1,N,2):
        sum += f(a+i*h)
    sum*=h
    return sum

def cv_gaussian(b,N):
    x,w=gaussxwab(N,b,1) #calculate the weights and positions
    s=0.0
    for l in range(N):
        s+=f(x[l])*w[l] #do integration  
    return s

def part1b(a):
    N=100
    error=1
    accuracy = 1e-6
    trap_sum_old=cv_trapezoidal(a,N)
    #print("N=",a,N,trap_sum_old)

    while(error>accuracy):
        N*=2
        trap_sum = trap_sum_old/2. + Ti(a,N)
        error=1/3*abs(trap_sum-trap_sum_old)
        trap_sum_old=trap_sum
        #print("N=",a,N,trap_sum)

    #print("a=",a,N,trap_sum)
    
    return trap_sum
print("part (1a) -30 marks")

r=[10,50,100,1000,5000]
for N in r:
    print("N=",N,"I=",cv_gaussian(0,N))
    
print("part (1b) -40 marks")
r=[0.2,0.1,0.01,0.001]
for a in r:
    print("a=",a,"I=",part1b(a))

y=linspace(log(0.0001),0,100)
r=exp(y)

result=[] 
for a in r: 
    result.append(part1b(a))
    
plot(log(r),result)
ylim(1.0,2.1)
xlabel("log(a)")
ylabel("I(a)")
show()

print("It seems there is a limit exists for a-->0 and it is slightly larger than 2.")
