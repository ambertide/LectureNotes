import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt
import seaborn as sns


sns.set_style("white")
x = np.linspace(44, 100, 1000)
n_square = x**(1/3)
n_sqrt = x ** (1/2)
n = 1.3 * np.sin(0.25 * x) + 6

ax, fig = plt.subplots()

fig.plot(x, n_square, label="$c_1$")
fig.plot(x, n_sqrt, label="$c_2$")
fig.plot(x, n, label="$g(x)$")
fig.legend()
sns.despine()
plt.show()



