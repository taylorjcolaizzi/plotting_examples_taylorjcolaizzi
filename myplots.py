# generates plots called canvas1_py.png and canvas2_py.pdf for the computational physics course

import matplotlib.pyplot as plt
import numpy as np
import random
import math

N_points = 10000
n_bins = 100
xmin = 50
xmax = 150
sigma = 6.04
mean = 100

rng = np.random.default_rng(2025) # year is seed

# ~~~~~~~~~~~~~~~~~~~~ making first plot ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# just a histogram. 10000 data points from normal distribution
# centered at 100 with width 6. But we want to plot the error
# bars, not the histogram, so we'll need to calculate that
# ourself via matplotlib.

fig = plt.figure()

normal = rng.standard_normal(N_points)*sigma + mean

plt.hist(normal, bins=n_bins, range=(xmin, xmax), histtype='step', label='normal distribution')
plt.title('random gauss')
plt.xlabel('x')
plt.ylabel('frequency')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('canvas1_py.png')

plt.clf()

