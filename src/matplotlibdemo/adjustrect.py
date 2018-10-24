import numpy as np
import matplotlib.pyplot as plt

'''调整 matplotlib 子图的大小'''

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)


plt.figure()

rect1 = [0.14, 0.35, 0.77, 0.6] # [左, 下, 宽, 高] 规定的矩形区域 （全部是0~1之间的数，表示比例）
rect2 = [0.14, 0.05, 0.77, 0.2]

ax1 = plt.axes(rect1)
ax2 = plt.axes(rect2)

ax1.plot(x1, y1, '-og', ms=3)
ax2.plot(x2, y2, '-ob', ms=3)

plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
#
# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 2.0)
#
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.axes([0.14, 0.35, 0.77, 0.6])
# plt.plot(x1, y1, 'yo-')
#
# plt.axes([0.14, 0.05, 0.77, 0.2])
# plt.plot(x2, y2, 'r.-')
#
# plt.show()