# -*- coding: utf-8 -*-
"""

A colored scatter plot using matplotlib with histograms on both axes.
Inspired by example code by Matplotlib here:
https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py

Example data is included.

Created on Wed Aug 26 2020

author: DavidLitwin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('sample_data.csv')
df_reg = pd.read_csv('data_regression.csv')

m = df_reg['m'][0]
b = df_reg['b'][0]

x = np.linspace(0, max(df['X']), 10)
y_theory = x - 1
y_reg = m*x + b

# definitions for the axes
left, width = 0.1, 0.6
bottom, height = 0.1, 0.6
hist_spacing = 0.005
hist_width = 0.15
cbar_spacing = 0.01
cbar_width = 0.03

# axes specs
rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + hist_spacing, width, hist_width]
rect_histy = [left + width + hist_spacing, bottom, hist_width, height]
rect_cb = [left + width + hist_spacing + hist_width + cbar_spacing, bottom, cbar_width, height]

# start with a rectangular figure
fig = plt.figure(figsize=(8, 8))

# add axes
ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)
ax_histx = plt.axes(rect_histx)
ax_histx.tick_params(direction='in', labelbottom=False)
ax_histy = plt.axes(rect_histy)
ax_histy.tick_params(direction='in', labelleft=False)
ax_cb = plt.axes(rect_cb)

# make the scatter plot:
sc = ax_scatter.scatter(df['X'], 
              df['Y'], 
              s=8, 
              alpha=0.5, 
              c=df['Z'], 
              cmap='plasma',
              vmin=0.0,
              vmax=0.6,
              )
ax_scatter.plot(x, y_theory, 'k--', label='$X - 1$')
ax_scatter.plot(x, y_reg, 'b-', label='%.2f $X - 1$'%m)
ax_scatter.set_xlabel('$X$')
ax_scatter.set_ylabel('$Y$')
ax_scatter.set_ylim((-1.2, max(df['Y']) + 0.1*max(df['Y'])))
cbar = fig.colorbar(sc, cax=ax_cb, label='$Z$', orientation="vertical")
cbar.solids.set_edgecolor("face")
ax_scatter.legend(frameon=False)

# set limits 
binwidth = 5
ymax = max(df['Y'])
ymin = -1.2
xmax = max(df['X'])
xmin = 0.0
ax_scatter.set_xlim((xmin, xmax))
ax_scatter.set_ylim((ymin, ymax))

# make histogram
ax_histx.hist(df['X'], bins=100, density=False, color='0.5')
ax_histy.hist(df['Y'], bins=100, density=False, color='0.5', orientation='horizontal')

# set histogram limlits
ax_histx.set_xlim(ax_scatter.get_xlim())
ax_histy.set_ylim(ax_scatter.get_ylim())

## option to hide histogram axes
# ax_histx.spines['right'].set_visible(False)
# ax_histx.spines['left'].set_visible(False)
# ax_histx.spines['top'].set_visible(False)
# ax_histy.spines['right'].set_visible(False)
# ax_histy.spines['top'].set_visible(False)
# ax_histy.spines['bottom'].set_visible(False)

plt.show()


