import numpy as np

def inp():
    # shellで切り出し済みのデータを読み込む
    print('Input node file name >>>>')
    f_name_node = input().rstrip() # 節点値のデータ

    print('Input nbool file name >>>>')
    f_name_nbool = input().rstrip() # nbool

    ############################################

    elem_node = np.loadtxt(f_name_nbool,
                        delimiter=",",
                        skiprows=0,
                        usecols=(3,4,5,6)
                        # usecols=(1,2,3,4)
                        )
    node_data = np.loadtxt(f_name_node,
                        delimiter=",",
                        skiprows=0,
                        usecols=(1,2)
                        )

    nelem = int(elem_node.shape[0])

    elem_node_data = np.zeros((nelem,4,2))

    for i in range(int(nelem)):
        elem_node_data[i][0] = node_data[int(elem_node[i][0])]
        elem_node_data[i][1] = node_data[int(elem_node[i][1])]
        elem_node_data[i][2] = node_data[int(elem_node[i][2])]
        elem_node_data[i][3] = node_data[int(elem_node[i][3])]

    return elem_node_data
