# -*- coding: utf-8 -*-
"""
Lab5
Created on Sun Mar 12 14:34:03 2017

@author: HyTang
"""
# Import
import numpy
from numpy import pi,sin,linspace
from scipy.integrate import quad
from pylab import plot,show,xlabel,ylabel,legend
# Constant
a = 10 # in ev
Pi2H2ML2 = 1.5040655 # in ev
M8APi2 = -8*a/pi**2 # in ev

# Func
def Sin2(x,m,n):
    return sin(pi*m*x)*sin(pi*n*x)
    
def xSin2(x,m,n):
    return x*sin(pi*m*x)*sin(pi*n*x)
    
def HmnManul(m,n):
    value = 0.0
    if m == n: # equal
        value = a/2+Pi2H2ML2*n**2
    elif (m+n)%2==1: # even + odd
        value = M8APi2*m*n/(m**2-n**2)**2
    else:   # both even or odd
        value = 0.0
    return value

def HmnInt(m,n):
    IValue = quad(Sin2,0,1,args=(m,n))
    IIValue = quad(xSin2,0,1,args=(m,n)) 
    return 2.0*n**2*Pi2H2ML2*IValue[0] + 2.0*a*IIValue[0]

def PDFCpt(x,w,N): # x in normalized form
    value = 0.0
    for ii in range(0,N):
        value += w[ii]*sin(pi*(ii+1)*x)
    return value*value
        
    
#### Main ####
# Part 2 ######################################################################
print('Part 2: Hmn')
for mm in range(1,6):
    for nn in range(1,6):
        print("m = %d, n = %d, HmnManul = %.5f, HmnInt = %.5f"%(mm,nn,HmnManul(mm,nn),HmnInt(mm,nn)))

# Part 3 ######################################################################        
print('\n')
print('Part 3: Hmn m,n = 10')
H10Matrix = numpy.zeros([10,10])
for mm in range(0,10):
    for nn in range(0,10):
        H10Matrix[mm,nn] = HmnManul(mm+1,nn+1)
# print(HMatrix)
H10Eig = numpy.linalg.eigvalsh(H10Matrix)
print('H10 eigenvalue: ',H10Eig) 

# Part 4 ######################################################################
print('\n')
print('Part 4: Hmn m,n = 100')
H100Matrix = numpy.zeros([100,100])
for mm in range(0,100):
    for nn in range(0,100):
        H100Matrix[mm,nn] = HmnManul(mm+1,nn+1)
H100Eig = numpy.linalg.eigvalsh(H100Matrix)
print('H100 eigenvalue: ',H100Eig[0:10])

e100M10 = linspace(0,0,10)
for ii in range(0,10):
    e100M10[ii] = abs(H100Eig[ii]-H10Eig[ii])/H100Eig[ii]*100
print('The proportional error are (in percentage): ',e100M10)     
print('The result is accurate enough for system in low energy state')

# Part 5 ######################################################################
# result based on H10Matrix
print('\n')
print('Part 5: PDF of Ground and 2 Excited States')
Eig10, EigV10 = numpy.linalg.eigh(H10Matrix)
# PDF Generate
SPNum = 101
PDF1 = linspace(0,0,SPNum)
PDF2 = linspace(0,0,SPNum)
PDF3 = linspace(0,0,SPNum)

x = linspace(0,1,SPNum)
for ii in range(0,SPNum):
    PDF1[ii] = PDFCpt(x[ii],EigV10[:,1],10)
    PDF2[ii] = PDFCpt(x[ii],EigV10[:,2],10)
    PDF3[ii] = PDFCpt(x[ii],EigV10[:,3],10)
    
# Norm Constant Cpt
PDF1Sum = numpy.sum(PDF1[0:SPNum])/(SPNum-1)
PDF2Sum = numpy.sum(PDF2[0:SPNum])/(SPNum-1)
PDF3Sum = numpy.sum(PDF3[0:SPNum])/(SPNum-1)
PDF1Norm = PDF1/PDF1Sum
PDF2Norm = PDF2/PDF2Sum
PDF3Norm = PDF3/PDF3Sum

# Plot
plot(x*5,PDF1Norm,label="G") 
plot(x*5,PDF2Norm,label="1") 
plot(x*5,PDF3Norm,label="2")
legend(loc="upper left")
xlabel("x(A)")
ylabel('PDF')
show()
# Normalization Check
PDF1NormSum = numpy.sum(PDF1Norm[0:SPNum])/(SPNum-1)
PDF2NormSum = numpy.sum(PDF2Norm[0:SPNum])/(SPNum-1)
PDF3NormSum = numpy.sum(PDF3Norm[0:SPNum])/(SPNum-1)
print('Norm Check for G, 1 and 2: ',PDF1NormSum,',',PDF2NormSum,',',PDF3NormSum)
