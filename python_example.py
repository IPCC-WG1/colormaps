#python example

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

#read the txt file
rgb_data_in_the_txt_file = np.loadtxt("cmap_example.txt")

#create the colormap
my_colormap = mcolors.LinearSegmentedColormap.from_list('colormap', rgb_data_in_the_txt_file)

#example use in a plot. "my_colormap" can be used just like any other colormap in matplotlib.
N = 10
x = np.linspace(0., 10., N)
y = np.linspace(0., 10., N)
z = np.random.uniform(-2., 2., size=(N,N))

levels = 8
plt.contourf(x, y, z, levels, cmap=my_colormap)
plt.colorbar()
plt.show()
