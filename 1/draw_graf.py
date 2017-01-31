import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)

# # グラフの描画
plt.plot(x,y)
plt.show()

## sin & cosのグラフ
# x = np.arange(0,6,0.1) # 0 ~ 6までを0.1刻みで生成
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1,label="sin")
# plt.plot(x,y2,label="cos",linestyle="--")
# plt.xlabel("x") # x軸
# plt.ylabel("y") # y軸
# plt.title("sin & cos") #title
# plt.legend() #右上に補助をつける
# plt.show()