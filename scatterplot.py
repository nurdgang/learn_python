import numpy as np
import pandas
from scipy import stats
import matplotlib.pyplot as plt

x = np.random.normal(1, 20, 250)
y = np.random.normal(1, 20, 250)

plt.scatter(x, y)
plt.show()
