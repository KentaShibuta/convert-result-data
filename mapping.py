from sympy.solvers import solve
from sympy import Symbol
import numpy as np

def map(node_val_x, real_point):
    xi = Symbol('xi')
    eta = Symbol('eta')

    equation1 = node_val_x[0][0]*0.25*(1-xi)*(1-eta) + node_val_x[1][0]*0.25*(1+xi)*(1-eta) + node_val_x[2][0]*0.25*(1+xi)*(1+eta) + node_val_x[3][0]*0.25*(1-xi)*(1+eta) - real_point[0]
    equation2 = node_val_x[0][1]*0.25*(1-xi)*(1-eta) + node_val_x[1][1]*0.25*(1+xi)*(1-eta) + node_val_x[2][1]*0.25*(1+xi)*(1+eta) + node_val_x[3][1]*0.25*(1-xi)*(1+eta) - real_point[1]
    ans = solve([equation1, equation2],dict=True)
    if ans[0][xi]<=1 and ans[0][xi]>=-1 and ans[0][eta]<=1 and ans[0][eta]>=-1:
        ans2=np.array([ans[0][xi],ans[0][eta]])
        return ans2
    else:
        ans2=np.array([ans[1][xi],ans[1][eta]])
        return ans2