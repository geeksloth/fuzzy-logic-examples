from matplotlib import pyplot as plt
plt.rc("figure", figsize=(5, 5))

from fuzzylogic.classes import Domain
from fuzzylogic.functions import R, S, alpha

T = Domain("test", 0, 30, res=0.1)

T.up = R(1,10)
T.up.plot()
plt.show()

T.down = S(20, 29)
T.down.plot()
plt.show()

T.polygon = T.up & T.down
T.polygon.plot()
plt.show()

T.inv_polygon = ~T.polygon
T.inv_polygon.plot()
plt.show()