"""
Author: Faycal Kilali
Citation: Claude.AI (Anthropic, @025) for assistance with display and save_finaL_state functions.
Project: Conway's Game of Life
Version: 1.0
"""

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors

def display(matrix, generation=0, pause_time=0.5):
    """
    Displays the current state of Conway's Game of Life using matplotlib.
    Alive cells are yellow, and dead cells are black.
    AI Critique: I added grid lines and the ability to save the figure per generation in the same directory. The AI failed to make the plots look like CoL so I went out of my way to make the cells that are alive yellow, and the dead ones black.

    :param matrix: 2D matrix representing the current state
    :param generation: Current generation number
    :param pause_time: Time in seconds to pause before next update
    """
    plt.figure(figsize=(6,6))  # Set figure size explicitly

    # Create a custom colormap: 0 -> black, 1 -> yellow
    cmap = mcolors.ListedColormap(['black', 'yellow'])

    # Display the matrix
    plt.imshow(matrix, cmap=cmap, interpolation='none')

    # Set title
    plt.title(f"Conway's Game of Life - Generation {generation}", fontsize=12)

    # Configure grid
    ax = plt.gca()
    ax.set_xticks([x - 0.5 for x in range(len(matrix[0]) + 1)], minor=False)
    ax.set_yticks([y - 0.5 for y in range(len(matrix) + 1)], minor=False)
    ax.grid(True, color='white', linestyle='-', linewidth=1)

    # Hide tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis='both', which='both', length=0)

    # Save the figure before showing
    filename = f"generation_{generation}.png"
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    print(f"Saved {filename}")

    # Show the plot
    plt.draw()
    plt.pause(pause_time)
    plt.close()  # Close figure to prevent overlap

def save_final_state(matrix, output_file="final_state.txt"):
    """
    Saves the final state of the simulation to a text file.
    AI Critique: no issues here.

    :param matrix: 2D matrix representing the final state
    :param output_file: Path to the output file
    """

    # Open file 'final_state.txt' then write to it the final state matrix.
    with open(output_file, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')