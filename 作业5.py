import numpy as np 
NONE = 1000

def prim(V, E, sel, wait, T):
    min_ = []
    for i in sel:
        possible_j = [j for j in range(6) if j not in sel]
        possible_edges = [E[i][j] for j in possible_j]
        edges_i = np.array([[j, edge] for j, edge in zip(possible_j, possible_edges)])
        min_j_index = np.argmin(edges_i[:, 1])
        min_j = edges_i[min_j_index][0]
        min_.append([min_j, E[i][min_j], i])
    min_ = np.array(min_)
    min_from = min_[np.argmin(min_[:,1])][2]
    new_sel = min_[np.argmin(min_[:,1])][0]
    edge_sel = E[min_from][new_sel]
    T.append((min_from, new_sel, edge_sel))

    sel.append(new_sel)
    wait.remove(new_sel)
    v_from = V[min_from]
    v_to = V[new_sel]
    print(v_from, '---{}---'.format(edge_sel), v_to)


def main():
    V = ['L', 'M', 'N', 'Pa', 'Pe', 'T']
    E = np.array([
        [NONE, 56, 35, 21, 51, 60],
        [56, NONE, 21, 57, 78, 70],
        [35, 21, NONE, 36, 68, 68],
        [21, 57, 36, NONE, 51, 61],
        [51, 78, 68, 51, NONE, 13],
        [60, 70, 68, 61 ,13, NONE]
    ])
    sel = [0]
    wait = [i for i in range(6) if i not in sel]
    T = []
    while wait:
        prim(V, E, sel, wait, T)
    print(T)
    print('Sum Weights:{}'.format(sum(np.array(T)[:, 2])))

if __name__ == '__main__':
    main()