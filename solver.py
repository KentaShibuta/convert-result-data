import discrimination
import mapping
import input_data
import create_new_mesh
import numpy as np

if __name__ == "__main__":

    elem_node_data = input_data.inp()
    node_val = create_new_mesh.new_mesh()

    #cul_val = np.zeros((int(node_val.shape[0]),2))
    cul_val = np.zeros((121,2))
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
                
                print(i)
                print("in")
                break

    np.savetxt('./np_savetxt.csv', cul_val, delimiter=',')

