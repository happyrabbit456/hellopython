import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0, 10, 100)
b = np.exp(-a)
plt.plot(a, b)
plt.show()


# from pylab import *
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
# plot(X,C)
# plot(X,S)
# show()
