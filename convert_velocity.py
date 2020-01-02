import numpy as np
import math
import cmath

def conv_v(cul_point, v_data):
    vx = v_data[0][0]*0.25*(1-cul_point[0])*(1-cul_point[1]) + v_data[1][0]*0.25*(1+cul_point[0])*(1-cul_point[1]) + v_data[2][0]*0.25*(1+cul_point[0])*(1+cul_point[1]) + v_data[3][0]*0.25*(1-cul_point[0])*(1+cul_point[1])
    vy = v_data[0][1]*0.25*(1-cul_point[0])*(1-cul_point[1]) + v_data[1][1]*0.25*(1+cul_point[0])*(1-cul_point[1]) + v_data[2][1]*0.25*(1+cul_point[0])*(1+cul_point[1]) + v_data[3][1]*0.25*(1-cul_point[0])*(1+cul_point[1])

    v = np.array([vx,vy])

    return v