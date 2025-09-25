# generates plots called canvas1_py.png and canvas2_py.pdf for the computational physics course

import matplotlib.pyplot as plt
import numpy as np
import random
import math
import ROOT as r

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
plt.ylabel('frequency')
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
axes[1].set_title('Gauss+offset')
axes[2].set_title('Gauss+offset2')
axes[3].set_title('Double Gaussian')

bins2 = bins[0].copy()
for i in range(N_points//3):
    bins2[random.randint(0, n_bins-1)] += 1
err2 = np.sqrt(bins2)
axes[1].errorbar(bc, bins2, yerr=err2, color="b", label = 'hist2', linestyle = 'none', fmt = '.')

bins3 = bins[0].copy()
# apply an offset to give us a 1/x^2 baseline
base2 = r.TF1("base2","1/x/x",1,10)
for i in range(N_points*30):
    x = base2.GetRandom()*10+40;
    bins3[int((x - xmin) / (xmax - xmin) * n_bins)] += 1
err3 = np.sqrt(bins3)
axes[2].set_yscale('log')
axes[2].set_ylim(100, 50000) # avoid log(0)
axes[2].errorbar(bc, bins3, yerr=err3, color="b", label = 'hist3', linestyle = 'none', fmt = '.')

bins4 = bins[0].copy()
fpeak = r.TF1("fpeak","exp(-0.5*(x-[0])*(x-[0])/[1]/[1])",50,150)
fpeak.SetParameters(100,20)
bins4 += np.histogram([fpeak.GetRandom() for _ in range(N_points//2)], bins=n_bins, range=(xmin, xmax))[0]
err4 = np.sqrt(bins4)
axes[3].errorbar(bc, bins4, yerr=err4, color="b", label = 'hist4', linestyle = 'none', fmt = '.')
# now do the legends, I guess
# more from copilot!
texts = [
    "Entries 10000\nMean 100\nStd Dev 6.04",
    "Entries 13333\nMean 100\nStd Dev 15.35",
    "Entries 310000\nMean 67.42\nStd Dev 20.65",
    "Entries 15000\nMean 99.86\nStd Dev 12.13",
]
for ax, txt in zip(axes, texts):
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.legend()
    at = AnchoredText(
        txt,
        loc='right',        # choose the corner
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
# plt.tight_layout()
plt.show()
plt.savefig("canvas2_py.pdf")