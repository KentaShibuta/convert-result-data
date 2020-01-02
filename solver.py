import discrimination
import mapping

if __name__ == "__main__":
    elem_data = [# 要素番号-物理空間における要素の四隅の座標値
        [[-1, -1],[2, -2],[4, 3],[-2,2]],
        [[0, 0],[1, 0],[1, 1],[0,1]]
    ]
    dot_data = [# グローバル節点番号-節点の座標値
        [3,2],
        [3,0],
        [-2,0],
        [0,2]
    ]

    for i in range(4):
        flag = -1
        for j in range(2):
            flag = discrimination.disc_in_element(elem_data[j],dot_data[i])
            if flag == 1:
                print("dot is in the element.")
                # ここで，該当する要素の中で線形補間されていることを利用して，dotでの速度を求める．
                ans = mapping.map(elem_data[j], dot_data[i])

                print(dot_data[i],elem_data[j],ans)
                flag = -1
                break  
            if j == 1:  
                print("dot is not the element.")
