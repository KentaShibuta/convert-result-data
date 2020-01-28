import numpy as np

def new_mesh():
    L_x = 1.0
    L_y = 1.0
    x_elem = 30
    y_elem = 30
    dx = L_x / x_elem
    dy = L_y / y_elem
    x_node = x_elem + 1
    y_node = y_elem + 1
    x = -0.5
    y = -0.5
    node_val = np.zeros((x_node*y_node,2))
    num = 0
    for j in range(y_node):
        for i in range(x_node):
            if i == 0:
                x=-0.5
            else:
                x = x + dx
            node_val[num][0]=x
            node_val[num][1]=y
            num = num + 1
        y = y + dy
        x = -0.5
    node_val_np = np.array(node_val)
    print(node_val_np)

    #np.savetxt('./np_savetxt.csv', node_val, delimiter=',')
    return node_val_np
