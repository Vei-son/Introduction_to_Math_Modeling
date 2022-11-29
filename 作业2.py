import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import leastsq
# 常数
V = 10

def Fun(params, input):
    V_0, tau = params
    t = input
    return (V - (V - V_0) * np.exp(- t / tau))

def error(params, input, true_val):
    # 这里只写偏差函数，具体平方是在leastsq中计算的
    # 仍然是符合最小二乘法要求
    pred_val = Fun(params, input)
    return pred_val-true_val

def main():
    # 样本数据
    t = np.array([0.5, 1, 2, 3, 4, 5, 7, 9])
    v = np.array([6.36, 6.48, 7.26, 8.22, 8.66, 8.99, 9.43, 9.63])
    # 给定初始的一组参数
    params0 = np.array([3, 1])
    s = Fun(params0, t)
    # 拟合，返回params
    # 传入leastsq参数为：1.残差函数，2.所需确定的函数参数对应的初始值，3.真实的输入数据
    params_fit = leastsq(error, params0, args=(t, v))
    # 拟合后的参数数组
    params_fit = params_fit[0]
    V_0, tau = params_fit
    print("V_0: {}, Tau: {}".format(V_0, tau))
    v_pred = Fun(params_fit, t)
    plt.plot(t, v, 'b', label='Sampled True Data')
    plt.plot(t, v_pred, 'o--', label='Fitted Data')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()