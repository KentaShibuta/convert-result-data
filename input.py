import numpy as np

print('Input node file name >>>>')
f_name_node = input().rstrip() # 可視化するファイル名

print('Input nbool file name >>>>')
f_name_nbool = input().rstrip() # 可視化するファイル名

df_node = np.loadtxt(f_name_node,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,2)
                    )
#array_info(df_node)

df_nbool = np.loadtxt(f_name_nbool,
                    delimiter=",",
                    skiprows=0,
                    usecols=(0,1,3,4,5,6)
                    )

