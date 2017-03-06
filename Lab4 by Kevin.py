# PHYS 3142 Lab4 Suggested solution by KWOK King Wai, Kevin

from numpy import array, zeros,abs
from numpy.linalg import solve
from banded import banded


print ("====================== part 1a ======================")
A = array([[3,-1,-1],[-1,4,-1],[1,1,-3]],ﬂoat)
w = array([5,5,0],ﬂoat)
v = solve(A,w)
print("The answer is V1 =",v[0],"V, V2 =",v[1],"V, V3 =",v[2],"V.")

print ("====================== part 1c ======================")
A2 = array([[3,-1,-1,0,0,0],[-1,4,-1,-1,0,0],[-1,-1,4,-1,-1,0],[0,-1,-1,4,-1,-1],[0,0,-1,-1,4,-1],[0,0,0,-1,-1,3]],float)
w2 = array([5,5,0,0,0,0],float)
v2 = solve(A2,w2)
print("The answer is V1 =",v2[0],"V, V2 =",v2[1],"V, V3 =",v2[2],"V, V4 =",v2[3],"V, V5 =",v2[4],"V, V6 =",v2[5],"V.")

print ("====================== part 1d ======================")
###### Fast Method ######
N = 10000
A3 = zeros([5,N],float)
for i in range(2):
    for j in range(N):
        A3[i][j] = -1
        A3[i+3][j] = -1
        A3[2][j] = 4

A3[0][0]=0
A3[0][1]=0
A3[1][0]=0
A3[3][N-1]=0
A3[4][N-1]=0
A3[4][N-2]=0
A3[2][0]=3
A3[2][N-1]=3

w3 = zeros(N,float)
w3[0] = 5
w3[1] = 5

print(banded(A3,w3,2,2))

###### Slow method ######
'''
N = 10000
A3 = zeros([N,N],float)
w3 = zeros(N,float)

for i in range(N):
    for j in range(N):
        if(i==j):
            A3[i,j] = 4
        elif((abs(i-j)==1) or (abs(i-j)==2)):
            A3[i,j] = -1
A3[0,0] = 3
A3[N-1,N-1] = 3
w3[0] = 5
w3[1] = 5

up = 2
down = 2
B = zeros((up+down+1,N),float)
for i in range(up+down+1):
    for j in range(N):
        if((j-up+i>=0) and (j-up+i<N)):
            B[i,j] = A3[j-up+i,j]

print (banded(B,w3,up,down))
'''