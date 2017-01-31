# 恒等関数はそのままの値を返したのに比べて、ソフトマックス関数は0~1の実数になり総和が１になる。
# このことからそれぞれを確立として見ることができる

import numpy as np

def softmax(x):
	c = np.max(x)
	exp_a = np.exp(a-c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a

	return y

if __name__ == "__main__":
	a = np.array([0.3,2.9,4.0])
	y = softmax(a)
	print(y*100) # [ 0.01821127  0.24519181  0.73659691] -> 1.8%,24.5%,73.6%
	print(np.sum(y)) # 1