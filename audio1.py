import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
#fs,data=wav.read('prasanna.wav')
fs1,d8k=wav.read('/home/rgukt/Desktop/prasanna.wav')
fs2,d5k=wav.read('/home/rgukt/Desktop/prasanna5k.wav')
fs3,d10k=wav.read('/home/rgukt/Desktop/prasanna10.wav')
fs4,d40k=wav.read('/home/rgukt/Desktop/prasanna40.wav')
print(fs1,len(d8k))
print(d8k)
t=np.arange(0,len(d8k)/fs1,1.0/fs1)
t1=np.arange(0,len(d5k)/fs2,1.0/fs2)
t2=np.arange(0,len(d10k)/fs3,1.0/fs3)
t3=np.arange(0,len(d40k)/fs4,1.0/fs4)
plt.subplot(1,4,1)
plt.plot(t,d8k)
plt.subplot(1,4,2)
plt.plot(t1,d5k)
plt.subplot(1,4,3)
plt.plot(t2,d10k)
plt.subplot(1,4,4)
plt.plot(t3,d40k)
plt.show()
#wav.write('/home/rgukt/Desktop/slow.wav',int(fs1*0.5),d8k)  #expand
#wav.write('/home/rgukt/Desktop/prasu_fast.wav',fs1*2,d8k)   #compress
#wav.write('/home/rgukt/Desktop/slow2.wav',4000,d8k)  #expand
