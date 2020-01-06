import numpy as np

def inp_v():
    # 2回もnboolのデータを読み込みたくない
    print('Input nbool file name >>>>')
    f_name_nbool = input().rstrip() # 可視化するファイル名

    print('Input velocity file name >>>>')
    f_name_velocity = input().rstrip() # 可視化するファイル名

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
    node_velocity = np.loadtxt(f_name_velocity,
                        delimiter=",",
                        skiprows=0,
                        usecols=(1,2)
                        )


    nelem = int(elem_node.shape[0])

    elem_node_velocity = np.zeros((nelem,4,2))

    #print(nelem)

    for i in range(int(nelem)):
        elem_node_velocity[i][0] = node_velocity[int(elem_node[i][0])]
        elem_node_velocity[i][1] = node_velocity[int(elem_node[i][1])]
        elem_node_velocity[i][2] = node_velocity[int(elem_node[i][2])]
        elem_node_velocity[i][3] = node_velocity[int(elem_node[i][3])]

    #np.save('./output.txt', elem_node_data)
    #np.savetxt('./np_savetxt.csv', elem_node_data, delimiter=',')
    return elem_node_velocity
