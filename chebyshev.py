import math
import numpy as np
import matplotlib.pyplot as plt
p=0.8#input("enter pass band amp")#0.707
s=0.02#input("enter stop band amp")#0.01
ws=81#input("enter stop band freq")#6282
wp=3.14#input("enter pass band freq")#3141
r=(1/(p*p))-1
e=np.sqrt(r)
print("e",e)
c=(1/(s*s))-1
d=np.sqrt(c)
cn1=(1/e)*d
print("cn1",cn1)
x=(ws/wp)
print("x",x)
l=np.arccosh(cn1)
v=np.arccosh(x)
N=6#np.ceil(l/v)
print(l/v)
print("order of filter",N)
for w in range(-1000,1000):
	if(w>wp):
		cn=np.cos(N*np.arccos(w))
		m=((cn**2)*(e**2))+1
		h=1/np.sqrt(m)
	if(w<wp):
		cn=np.cosh(N*np.arccosh(w))
		m=((cn**2)*(e**2))+1
		h=1/np.sqrt(m)
	plt.plot(h)
Apass=1000
plt.ylim(0,1)
plt.xlim(0, Apass)
plt.show()

