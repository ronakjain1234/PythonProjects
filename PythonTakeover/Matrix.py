import time # imports time
import random # imports random
import matplotlib.pyplot as plt # imports matplot library to plot figures
from matplotlib import colors # define the colormap


random.seed(time.time()) # randomizes inputs


def matrix(list, x): # defines the matrix function
    cmap = colors.ListedColormap(['yellowgreen', 'bisque', 'darkslategray', 'goldenrod']) # defines the colors of plots
    plt.figure(figsize=(7, 6)) # defines the matrix size
    plt.pcolor(list, cmap=cmap, edgecolors='k', linewidths=0.5, vmin=0, vmax=3) # defines the matrix edge details
    plt.savefig('spatial' + str(x) + '.pdf', bbox_inches='tight', pad_inches=0.02) # saves matrix with dimensions
    plt.show() # closes the figure


