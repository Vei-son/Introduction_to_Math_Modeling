from scipy.optimize import minimize
import numpy as np 

def get_ys(x1, x2, x3):
    y1 = max(0, x1 - 40)
    y2 = max(0, y1 + x2 - 60)
    y3 = max(0, y2 + x3 - 80)
    return y1, y2, y3

def obj_fun(params):
    # x是一个3*2 np.array[[x_1, y_1], [x_2, y_2], [x_3, y_3]]
    # params：a, b, c
    a, b, c = params
    fx = lambda x: a * sum(x[:]) + b * sum(x[:] ** 2) + c * sum(get_ys(x[0], x[1], x[2]))
    return fx

def get_constraints(borders):
    # 传入的borders表示等式或者不等式的最小值/最大值
    con1 = {'type': 'ineq', 'fun': lambda x: x[0] - borders[0]}
    con2 = {'type': 'ineq', 'fun': lambda x: x[1] + (get_ys(x[0], x[1], x[2]))[0] - borders[1]}
    con3 = {'type': 'ineq', 'fun': lambda x: x[2] + (get_ys(x[0], x[1], x[2]))[1] - borders[2]}
    cons = (con1, con2, con3)
    return cons

def main():
    # 搜索的初始值x1 x2 x3
    x = np.zeros(3)
    # 搜索边界
    bounds = [(0, None) for i in range(3)]
    # 不等式右端
    borders = (40, 60, 80)
    # 约束
    cons = get_constraints(borders)
    # a, b, c
    params = (1000, 0.2, 4)
    res = minimize(obj_fun(params), x, method='SLSQP', bounds=bounds, constraints=cons)
    if res.success:
        print("三个季度的总费用: {0:.2f}元；".format(res.fun))
        print("第一个季度生产{0:.0f}台, 第二个季度生产{1:.0f}台, 第三个季度生产{2:.0f}台发动机。".format(res.x[0], res.x[1], res.x[2]))
    else:
        print("抱歉,无法解决此问题!")

if __name__ == '__main__':
    main()