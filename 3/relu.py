# 最近でてきた関数
# ReLU関数。0以下は0で0を超えていれば実数を返す

import numpy as np
import matplotlib.pylab as plt

def relu(x):
	return np.maximum(0,x)

x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()