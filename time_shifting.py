import numpy as np
import cmath as cm
import matplotlib.pyplot as plt 

def DFT(x,N):
	i=len(x) # size of x
	print(i)
	j=cm.sqrt(-1)
	X=[]
	#w=np.linspace(0,2*np.pi,N)
	for k in range(N):
		sum=0
		for n in range(i):
			sum=sum+(x[n]*(cm.exp(((-j)*2*cm.pi*n*k)/N)))
		X.append(sum)
	
	print(X)
	plt.subplot(1,4,1)
	plt.stem(np.abs(X))
	plt.title("magnitude of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("|X[w]|")
	plt.subplot(1,4,2) 
	plt.stem(np.angle(X))
	plt.title("phase of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("/_X[w]")
	return(X)

def dtft(x,N):
    xw=[]
    j=cm.sqrt(-1)
    n=len(x)
    w=np.linspace(0,2*np.pi,N)
    for i in range(0,N):
        sum=0
        w_temp=w[i]
        for k in range(0,n):
            sum=(sum+(x[k]*np.exp((-j)*w_temp*k)))

        xw.append(sum)

    plt.subplot(1,4,3)
    plt.plot(w,np.abs(xw))
    plt.title("magnitude of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("|x[w]|")
    plt.subplot(1,4,4) 
    plt.plot(w,np.angle(xw))
    plt.title("phase of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("/_x[w]")
    return(xw)

N=int(input("enter no. of samples"))  #choose 8-point or 4-point dft
x=np.array(input("enter values of x[n]"))

DFT(x,N)

dtft(x,4)

plt.show()


