from matplotlib import pyplot as plt
plt.rc("figure", figsize=(5, 5))
from fuzzylogic.classes import Domain, Set
from fuzzylogic.functions import (sigmoid, gauss, trapezoid, 
                             triangular_sigmoid, rectangular)

T = Domain("Mixed", 0, 100, res=1)

T.sigmoid = sigmoid(1,1,20)
T.sigmoid.plot()

T.gauss = gauss(10, 0.01, c_m=1.0)
T.gauss.plot()

T.trapezoid = trapezoid(25, 30, 35, 40, c_m=0.9)
T.trapezoid.plot()

T.triangular_sigmoid = triangular_sigmoid(40, 70, c=55)
T.triangular_sigmoid.plot()

T.rectangular = rectangular(low=80, high=95, c_m=0.5)
T.rectangular.plot()
plt.show()