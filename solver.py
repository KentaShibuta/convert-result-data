import discrimination
import mapping
import input_data
import create_new_mesh
import input_v
import numpy as np

if __name__ == "__main__":

    elem_node_data = input_data.inp()
    node_val = create_new_mesh.new_mesh()
    elem_node_velocity = input_v.inp_v()

    print(elem_node_velocity)
    
    #cul_val = np.zeros((int(node_val.shape[0]),2))
    cul_val = np.zeros((121,2))
    velocity = np.zeros((121,2))
    num = 0
    #for i in range(int(node_val.shape[0])):
    for i in range(121):
        flag = -1
        #for j in range(int(elem_node_data.shape[0])):
        for j in range(4500):
            flag = discrimination.disc_in_element(elem_node_data[j],node_val[i])
            #if i==6:
            #    print(elem_node_data[j], node_val[i])
            if flag == 1:
                
                # ここで，該当する要素の中で線形補間されていることを利用して，dotでの速度を求める．
                cul_val[i] = mapping.map(elem_node_data[j], node_val[i])
                velocity[i][0] = elem_node_velocity[j][0][0]*0.25*(1-cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][1][0]*0.25*(1+cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][2][0]*0.25*(1+cul_val[i][0])*(1+cul_val[i][1]) + elem_node_velocity[j][3][0]*0.25*(1-cul_val[i][0])*(1+cul_val[i][1])
                velocity[i][1] = elem_node_velocity[j][0][1]*0.25*(1-cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][1][1]*0.25*(1+cul_val[i][0])*(1-cul_val[i][1]) + elem_node_velocity[j][2][1]*0.25*(1+cul_val[i][0])*(1+cul_val[i][1]) + elem_node_velocity[j][3][1]*0.25*(1-cul_val[i][0])*(1+cul_val[i][1])
                print(i)
                print("in")
                break

    np.savetxt('./conv_velocity.csv', velocity, delimiter=',')
    np.savetxt('./conv_point.csv', node_val, delimiter=',')
