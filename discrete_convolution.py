import numpy as np
import math

n1=int(input("enter length of m"))
n2=int(input("enter length of n"))

x=np.array(input("enter value"))	
	#x.append(a)
print(type(x))

#h=[]
h=np.array(input("enter value"))
	#h.append(b)

y=[]
for n in range(n1+n2-1):
       sum=0
       for k in range(n1):
             if (n-k>=0)and(n-k<=n2-1):
                   m=np.multiply(x[k],h[n-k])
                   sum=sum+m
       y=np.append(y,sum)
			
print(y) 



#y[0]=x[0]*h[0]
#y[1]=x[1]*h[0]+x[0]*h[1]
