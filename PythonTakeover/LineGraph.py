import matplotlib.pyplot as plt # imports the matplot library


def plotDynamics(rabbits, alligators, time): # defines function which plots line graph rabbits & alligators over time
    fig, axes = plt.subplots(figsize=(7, 6)) # defines the figure size
    axes.plot(time, rabbits, label='rabbits', color='bisque') # defines the color of the rabbits line and labels
    axes.plot(time, alligators, label='alligators', color='darkslategray') # defined the color of the alligators line and labels
    axes.set_xlabel('Time (months)') # sets the x-axis label
    axes.set_ylabel('Number of Individuals') # sets the y-axis label
    #axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False) # make figure legend
    plt.savefig('LineGraph.pdf', bbox_inches='tight', pad_inches=0.02) # saves the figure with sized edges and spacing
    plt.close() # closes the figure window


def plotDynamics1(rabbits, alligators, python, time): # defines the function plotting species over time
    fig, axes = plt.subplots(figsize=(7, 6)) # defines the figure size
    axes.plot(time, rabbits, label='rabbits', color='bisque') # defines the color of plotting and label of rabbits
    axes.plot(time, alligators, label='alligators', color='darkslategray') # defines color and label of alligators
    axes.plot(time, python, label='python', color='goldenrod') # defines the color and label of pythons
    axes.set_xlabel('Time (months)') # sets the x-axis label
    axes.set_ylabel('Number of Individuals') # sets the y-axis label
    #axes.legend(bbox_to_anchor=(.3, 1), fontsize=13, fancybox=False, shadow=False, frameon=False) # make figure legend
    plt.savefig('LineGraph1.pdf', bbox_inches='tight', pad_inches=0.02) # saves the figure with sized edges and spacing
    plt.close() # closes the figure window

