# generates plots called canvas1_py.png and canvas2_py.pdf for the computational physics course

import matplotlib.pyplot as plt
import numpy as np
import random
import math

from matplotlib.offsetbox import AnchoredText

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

# adding a text box with mean and sigma. from copilot
textstr = '\n'.join((
    r'$\mathrm{Entries}=%d$' % (N_points, ),
    r'$\mathrm{Mean}=%.2f$' % (np.mean(normal), ),
    r'$\mathrm{Std Dev}=%.2f$' % (np.std(normal), )))
at = AnchoredText(textstr, prop=dict(size=10), frameon=True, loc='right')
at.patch.set_boxstyle("round,pad=0.3,rounding_size=0.2")
plt.gca().add_artist(at)

# back to my code...
plt.tight_layout()
plt.show()
plt.savefig('canvas1_py.png')

plt.clf()
# ~~~~~~~~~~~~~~~~~~~~ making second plot ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fig, axes = plt.subplots(2,2, figsize = (16, 16))

axes = axes.flatten() # make it easier to index
axes[0].errorbar(bc, yb, yerr=err, color="b", label = 'hist1', linestyle = 'none', fmt = '.') # now we are basically plotting a scatterplot with errorbars. No lines though
axes[0].set_title('random gauss')
axes[0].set_xlabel('x')
axes[0].set_ylabel('Frequency')
axes[0].legend()

textstr = '\n'.join((
    r'$\mathrm{Entries}=%d$' % (N_points, ),
    r'$\mathrm{Mean}=%.2f$' % (np.mean(normal), ),
    r'$\mathrm{Std Dev}=%.2f$' % (np.std(normal), )))
at = AnchoredText(textstr, prop=dict(size=10), frameon=True, loc='right')
at.patch.set_boxstyle("round,pad=0.3,rounding_size=0.2")
plt.gca().add_artist(at)

# now do the legends, I guess
# more from copilot!
texts = [
    "Panel A\nLine 2\nLine 3",
    "Panel B\nLine 2\nLine 3",
    "Panel C\nLine 2\nLine 3",
    "Panel D\nLine 2\nLine 3",
]
for ax, txt in zip(axes, texts):
    ax.set_title("Demo")

    at = AnchoredText(
        txt,
        loc='ight',        # choose the corner
        prop=dict(size=10),
        frameon=True,             # draw a frame
        borderpad=0.4,
        pad=0.2
    )
    # Customize the patch (box)
    at.patch.set_boxstyle("round,pad=0.4")
    at.patch.set_edgecolor("black")
    at.patch.set_linewidth(1.5)
    at.patch.set_facecolor("white")
    at.set_zorder(10)

    ax.add_artist(at)

# back to me writing
plt.tight_layout()
plt.show()
plt.savefig("canvas2_py.pdf")