import numpy as np 
import matplotlib.pyplot as plt 
BEGIN = -5
END = 5
STEPS = 10000
ori3 = np.array([1, -6, 5, -3])
y = np.poly1d(ori3)
x_ = np.linspace(BEGIN, END, STEPS)
y_ = y(x_)
noise = np.random.normal(0, 1, size=x_.shape)
y__ = y_ + noise
# =========================
# 三次多项式
# =========================
p3 = np.polyfit(x_, y__, 3)
# ================================================
# 二阶多项式
# ================================================
p2 = np.polyfit(x_, y__, 2)
# ================================================
# 四阶多项式
# ================================================
p4 = np.polyfit(x_, y__, 4)

print("原始系数：{}\n, 三阶拟合系数：{}\n, 二阶拟合系数：{}\n, 四阶拟合系数：{}".format(ori3, p3, p2, p4))

plt.plot(x_, y_, 'r', label='原始函数')
p3 = np.poly1d(p3)
y_p3 = p3(x_)
plt.plot(x_, y_p3, 'b--', label='三阶拟合效果')
p2 = np.poly1d(p2)
y_p2 = p2(x_)
plt.plot(x_, y_p2, 'y--', label='二阶拟合效果')
p4 = np.poly1d(p4)
y_p4 = p4(x_)
plt.plot(x_, y_p4, 'g--', label='四阶拟合效果')
plt.legend()
plt.show()