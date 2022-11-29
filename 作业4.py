import numpy as np 
import matplotlib.pyplot as plt 

"""
    使用k-means动态聚类算法对数据进行分析
"""
# 数据点个数
N = 8
# 类别数
CN = 3

def get_labels(A, C):
    def Euclid_dis(a, c):
        return np.sqrt(sum((a - c) ** 2))
    labels = np.zeros(N, dtype=int)
    for i in range(N):
        labels[i] = np.argmin([Euclid_dis(A[i], c) for c in C])
    return labels
            
def get_clusters(labels):
    C1_data = np.argwhere(labels == 0).reshape(-1)    # 由于返回的时候是按照多维思路来返回的所以是一个二维数组，而二维下标才是想要的值
    C2_data = np.argwhere(labels == 1).reshape(-1)
    C3_data = np.argwhere(labels == 2).reshape(-1)
    return C1_data, C2_data, C3_data


def get_Centers(A, labels):
    C1_data, C2_data, C3_data = get_clusters(labels)
    C1 = np.mean([A[i] for i in C1_data], axis=0)
    C2 = np.mean([A[i] for i in C2_data], axis=0)
    C3 = np.mean([A[i] for i in C3_data], axis=0)
    C = np.array([C1, C2, C3])
    return C

def main():
    # 被聚类的几个点
    A = np.array([[2, 10], [2, 5], [8, 4], [5,8],
         [7, 5], [6, 4], [1, 2], [4, 9]])
    # 初始化3个聚类中心
    C1, C2, C3 = A[0], A[3], A[6]
    C = np.array([C1, C2, C3])
    loop_time = 0
    done = False
    while not done:
        labels = get_labels(A, C)
        New_C = get_Centers(A, labels)
        if loop_time == 0:
            print("第一轮后：\n第一个聚类中心({},{})\t第二个聚类中心({},{})\t第三个聚类中心({}{})".format(
                New_C[0][0], New_C[0][1], New_C[1][0], New_C[1][1], New_C[2][0], New_C[2][1]
            ))
        if New_C.all() == C.all():
            done = True
        C == New_C
        loop_time += 1
    C1_data, C2_data, C3_data = get_clusters(labels)
    print("最后的三个簇:")
    print("第一类:",end=' ')
    for i in C1_data:
        print('A{}'.format(i),'({},{})'.format(A[i][0], A[i][1]),end=', ')
    print()
    print("第二类:",end=' ')
    for i in C2_data:
        print('A{}'.format(i),'({},{})'.format(A[i][0], A[i][1]),end=', ')
    print()
    print("第三类:",end=' ')
    for i in C3_data:
        print('A{}'.format(i),'({},{})'.format(A[i][0], A[i][1]),end=', ')

    # numpy花式索引，用逗号隔开
    plt.scatter(A[C1_data, 0], A[C1_data, 1],s = 300, c='b', alpha=0.5, label='第一类')
    plt.scatter(A[C2_data, 0], A[C2_data, 1],s = 100, c='r', alpha=0.5, label='第二类')
    plt.scatter(A[C3_data, 0], A[C3_data, 1],s = 200, c='y', alpha=0.5, label='第三类')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()