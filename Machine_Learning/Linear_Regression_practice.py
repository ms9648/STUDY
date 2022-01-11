# About Linear Regression

# 정규방정식
import matplotlib.pyplot as plt
import numpy as np

# rand(x, y) => 0에서 1 사이의 값으로 이루어 진 x by y 행렬을 만듦
# randn(x, y) => mu = 0, var = 1인 정규분포에서 값을 추출하여 x by y 행렬을 만듦
x = 2 * np.random.rand(100, 1) # 2를 곱해주었음.
y = 4 + 3*x + np.random.randn(100, 1)

x_b = np.c_[np.ones((100, 1)), x]

# θ = (X_T * X)-1 * X_T * Y 정규방정식
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
print(theta_best.shape) # 2 by 1 Matrix

x_new = np.array([[0], [2]])
x_new_b = np.c_[np.ones((2, 1)), x_new]

prediction = x_new_b.dot(theta_best)

# Y = θX ? or 아예 다른 개념

