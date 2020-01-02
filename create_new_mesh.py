import numpy as np

L_x = 0.01
L_y = 0.01
x_elem = 10
y_elem = 10
dx = L_x / x_elem
dy = L_y / y_elem
x_node = x_elem + 1
y_node = y_elem + 1
x = 0
y = 0
node_val = np.zeros((x_node*y_node,2))
num = 0
for j in range(y_node):
    for i in range(x_node):
        if i == 0:
            x=0
        else:
            x = x + dx 
        node_val[num][0]=x
        node_val[num][1]=y
        num = num + 1
    y = y + dy
    x = 0
print(node_val)

#np.savetxt('./np_savetxt.csv', node_val, delimiter=',')