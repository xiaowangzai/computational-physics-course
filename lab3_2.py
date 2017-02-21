#PHYS 3142 Lab 3 suggested solution
#By Ng Ka Ho, Tony
from numpy import log,exp,cos,pi,linspace
from gaussxw import gaussxwab
from pylab import plot,show,xlim,ylim,xlabel,ylabel

def f(kt,x,y):
    return -kt*log(1+exp(-2/kt*(cos(x)+cos(y))))
  
def cv_gaussian(kt,N):
    x,w=gaussxwab(N,-pi,pi)#calculate the weights and positions
    y,w1=gaussxwab(N,-pi,pi)
    s=0.0
    for l in range(N):
        for m in range(N):
            s+=f(kt,x[l],y[m])*w[l]*w1[m] #do integration
    return s
    
print("part (2) -30 marks")

N=100
kt=1

print("k_bT=1, F(T)=",cv_gaussian(kt,N))
result=[]
i=linspace(0.1,10,100)
for kt in i:
    result.append(cv_gaussian(kt,N))

plot(i,result)
xlabel("k_b T")
ylabel("F(T)")
show()    