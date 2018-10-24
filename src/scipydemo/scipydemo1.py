from scipy import *
import numpy as np
from pylab import *
a = zeros(1000)
a[:10]=1
b=fft(a)
plot(abs(b))
show()
