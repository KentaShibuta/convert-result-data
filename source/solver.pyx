from lib.discrimination import disc_in_element
from lib.mapping import map
from lib.input_data import inp
from lib.create_new_mesh import new_mesh
from lib.input_v import inp_v
import numpy as np

def solv():
    # inpファイルの読み込み
    elem_node_data = inp()
    node_val = new_mesh()
    elem_node_velocity = inp_v()

    cul_val = np.zeros((int(node_val.shape[0]),2))
    velocity = np.zeros((int(node_val.shape[0]),2))

    for i in range(int(node_val.shape[0])):
        flag = -1
        for j in range(int(elem_node_data.shape[0])):
            flag = disc_in_element(elem_node_data[j],node_val[i])
            if flag == 1:
                # ここで，該当する要素の中で線形補間されていることを利用して，dotでの速度を求める．
                cul_val[i] = map(elem_node_data[j], node_val[i])
                velocity[i][0] = elem_node_velocity[j][0][0]*0.25*(1-cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][1][0]*0.25*(1+cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][2][0]*0.25*(1+cul_val[i][0])*(1+cul_val[i][1]) + elem_node_velocity[j][3][0]*0.25*(1-cul_val[i][0])*(1+cul_val[i][1])
                velocity[i][1] = elem_node_velocity[j][0][1]*0.25*(1-cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][1][1]*0.25*(1+cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][2][1]*0.25*(1+cul_val[i][0])*(1+cul_val[i][1]) + elem_node_velocity[j][3][1]*0.25*(1-cul_val[i][0])*(1+cul_val[i][1])
                break

    np.savetxt('./conv_velocity.csv', velocity, delimiter=',')
    np.savetxt('./conv_point.csv', node_val, delimiter=',')
