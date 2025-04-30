import numpy as np  # standard alias for numpy
import matplotlib.pyplot as plt  # standard alias for matplotlib.pyplot
import scipy.stats as stats  # standard alias for scipy.stats

# Roll a dice a 1000 times
rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=1000)  # simulate rolling a dice 1000 times
rolls_matrix = np.array(rolls).reshape(1, 1000)  # reshape the rolls into a 1x1000 matrix

# Create the plot: 6 figures in 6 rows and 1 column
fig, axs = plt.subplots(6, 1, figsize=(10, 15))  # create a figure with 6 subplots in a single column
# Create a graph for x=roll index, y=roll value
for i in range(6):  # iterate over the dice numbers (1 to 6)
    axs[i] = plt.subplot(6, 1, i+1)  # create a subplot for each number of the dice
    axs[i].plot(rolls_matrix[0], 'o', markersize=2, color='blue')  # plot the rolls with blue dots
    axs[i].set_title(f'Dice Side {i+1}')  # set the title for each subplot
    axs[i].set_xlabel('Roll Index')  # set the x-axis label for each subplot
    axs[i].set_ylabel('Roll Value')  # set the y-axis label for each subplot
    axs[i].set_xlim(0, 1000)  # set the x-axis limits for each subplot
    axs[i].set_ylim(0, 7)  # set the y-axis limits for each subplot

plt.show()  # display the plot
