# 活性化関数の１つで、ステップ関数、階段関数と呼ばれる。
# 0を基準に、0か1を返す

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
	return np.array(x > 0,dtype=np.int)

x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()