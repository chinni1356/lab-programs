import scipy.io.wavfile as wav
import numpy as np
import math
from matplotlib import pyplot as plt
fs1,d8k=wav.read('/home/rgukt/Public/ECE/e2s2/DSP_LAB/Lab3/prasanna.wav')
print(fs1,len(d8k))
print (d8k)
t=np.arange(0,len(d8k)/fs1,1.0/fs1)
plt.plot(d8k)
plt.show()


