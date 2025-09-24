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

normal = rng.standard_normal(N_points)*sigma + mean
plt.figure()
bins = plt.hist(normal, bins=n_bins, range=(xmin, xmax), histtype='step', label='normal distribution')
plt.clf()
yb = bins[0]
xb = bins[1]
err = np.sqrt(yb)
#Calculate bin centers (you can probably find a smarter way to do this!)
bc=(xb[1:]-xb[:-1])/2+xb[:-1] # first minus last /2 (average) + last???
plt.xlabel('x')
plt.ylabel('Frequency')
plt.errorbar(bc, yb, yerr=err, color="b", label = 'hist1', linestyle = 'none', fmt = '.') # now we are basically plotting a scatterplot with errorbars. No lines though
plt.title('random gauss')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('canvas1_py.png')

plt.clf()
# ~~~~~~~~~~~~~~~~~~~~ making second plot ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

