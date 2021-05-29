import numpy as np

def disc_in_element(elem_data, dot_data):
    # 四角形の位置ベクトル
    p_a = np.array([elem_data[0][0],elem_data[0][1]])
    p_b = np.array([elem_data[1][0],elem_data[1][1]])
    p_c = np.array([elem_data[2][0],elem_data[2][1]])
    p_d = np.array([elem_data[3][0],elem_data[3][1]])

    # 位置を特定したい点の座標
    dot = np.array([dot_data[0],dot_data[1]])

    # 四角形の辺上のVectorの定義
    side_ab = p_b - p_a
    side_bc = p_c - p_b
    side_cd = p_d - p_c
    side_da = p_a - p_d

    # 求める点と四角形の各節点でのVectorの定義
    dot_side_a = dot - p_a
    dot_side_b = dot - p_b
    dot_side_c = dot - p_c
    dot_side_d = dot - p_d

    # 要素の内外を判別するために外積を計算
    cross_a = side_ab[0] * dot_side_a[1] - side_ab[1] * dot_side_a[0]
    cross_b = side_bc[0] * dot_side_b[1] - side_bc[1] * dot_side_b[0]
    cross_c = side_cd[0] * dot_side_c[1] - side_cd[1] * dot_side_c[0]
    cross_d = side_da[0] * dot_side_d[1] - side_da[1] * dot_side_d[0]

    if cross_a >= 0 and cross_b >= 0 and cross_c >= 0 and cross_d >= 0:
        return 1
    else:
        return -1