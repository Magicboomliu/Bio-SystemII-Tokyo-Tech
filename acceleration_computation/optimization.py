from cal_moment import getMaxMoment
import numpy as np
from scipy.optimize import minimize



def optimization(Am,l,maxmoment):
    fun = lambda x: abs((pow((x[0] / Am[0]), 3) + pow((x[1] / Am[1]), 3) + pow((x[2] / Am[2]), 3)))
    cons = ({'type': 'eq', 'fun': lambda x: l[0] * x[0] + l[1] * x[1] + l[2] * x[2] - maxmoment},
        {'type': 'ineq', 'fun': lambda x: x[0]},
        {'type': 'ineq', 'fun': lambda x: x[1]},
        {'type': 'ineq', 'fun': lambda x: x[2]}
        )

    x0 = np.array((0, 0, 0))
    res = minimize(fun, x0, method='SLSQP', constraints=cons)
    return res

if __name__ == "__main__":
    # Am = PCSA of each muscle
    #Jiang
    # Am = [24.4, 64.8, 185.5]
    # l = [-0.0257, -0.0263, -0.0271]
    # moment: -20
    #Li
    Am = [24.4, 64.8, 185.5]
    l = [-0.0419, -0.0427, -0.0435]
    #moment: -15

    print("陆兄弟はとても強いです")
    res = optimization(Am, l, getMaxMoment())
    print("final result: {}".format(res['x']))
