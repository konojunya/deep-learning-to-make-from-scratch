import numpy as np

#x = np.array([1.0,2.0,3.0])
#y = np.array([2.0,4.0,6.0])

#print(x+y) # [3.,6.,9.]
#print(x-y) # [-1.,-2.,-3.]
#print(x*y) # [2.,8.,18.]

## スカラー値での計算（jsでするならmap?）
## ブロードキャストという
#x = np.array([1.0,2.0,3.0])
#print(x/2.0) # [0.5,1.,1.5]

A = np.array([[1,2],[3,4]])
#print(A.shape) # (2,2)
#print(A.dtype) # int64
#B = np.array([[3,0],[0,6]])

#print(A+B)
#print(A*B)

# ブロードキャスト
#print(A*2)
#print(A*[1,2])

##アクセス
#print(A[0]) # [1,2]
#print(A[0][0]) # 1

#for row in A:
#	print(row)

## 1次元配列へ変換
#A = A.flatten()
#print(A) # [1,2,3,4]

## インデックスが0,2番目の要素を取得
#A = A.flatten()
#print(A[np.array([0,2])])

#print(A>10) # [[false,false],[false,false]]

# 1以上の数字だけを抽出
#print(A[A>1]) # [2,3,4]
