import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.random.normal(1, 20, 250)
y = np.random.normal(1, 20, 250)

slope, intercept, r, p, std_err = stats.linregress(x, y)
line_of_best_fit = list(map(myfunc, x)

def lineEq(x)
  return slope * x + intercept
                        
plt.scatter(x, y)
plt.plot(x, line_of_best_fit)
plt.show()


