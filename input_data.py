import numpy as np

def inp():
    print('Input node file name >>>>')
    f_name_node = input().rstrip() # 可視化するファイル名

    print('Input nbool file name >>>>')
    f_name_nbool = input().rstrip() # 可視化するファイル名

    ############################################
    #elem_node[nelem][4] # 要素番号と節点番号の対応
    #node_data[nnode][2]　
    # shellできざんできたファイルから読み取る．
    # shellできざまなくてもpythonできざむことができるよね．
    elem_node = np.loadtxt(f_name_nbool,
                        delimiter=",",
                        skiprows=0,
                        usecols=(3,4,5,6)
                        )
    # 要素番号と節点番号の対応

    node_data = np.loadtxt(f_name_node,
                        delimiter=",",
                        skiprows=0,
                        usecols=(1,2)
                        )
    nelem = int(elem_node.shape[0])

    elem_node_data = np.zeros((nelem,4,2))

    #print(nelem)

    for i in range(int(nelem)):
        elem_node_data[i][0] = node_data[int(elem_node[i][0])]
        elem_node_data[i][1] = node_data[int(elem_node[i][1])]
        elem_node_data[i][2] = node_data[int(elem_node[i][2])]
        elem_node_data[i][3] = node_data[int(elem_node[i][3])]

    print(elem_node_data)
    #np.save('./output.txt', elem_node_data)
    #np.savetxt('./np_savetxt.csv', elem_node_data, delimiter=',')
    return elem_node_data

