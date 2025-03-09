"""
Author: Faycal Kilali
Citation: Claude.AI (Anthropic, @025)
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
    # Clear previous plot
    plt.clf()

    # Create a custom colormap: 0 -> black, 1 -> yellow
    cmap = mcolors.ListedColormap(['black', 'yellow'])

    # Create a figure with a grid
    plt.imshow(matrix, cmap=cmap, interpolation='none')  # 'none' ensures sharp edges for cells
    plt.title(f"Conway's Game of Life - Generation {generation}", fontsize=12)

    # Customize grid appearance
    ax = plt.gca()

    # Set grid lines to align with cell edges
    ax.set_xticks([x - 0.5 for x in range(len(matrix[0]) + 1)], minor=False)  # Major ticks at cell boundaries
    ax.set_yticks([y - 0.5 for y in range(len(matrix) + 1)], minor=False)    # Major ticks at cell boundaries
    ax.grid(True, color='white', linestyle='-', linewidth=1)  # White grid lines for contrast

    # Remove tick marks and labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis='both', which='both', length=0)  # Hide tick marks

    # Ensure cells are square-shaped
    ax.set_aspect('equal')

    # Remove padding around the plot
    plt.tight_layout()

    # Draw the updated grid
    plt.draw()
    plt.pause(pause_time)

    # Save the figure
    filename = f"generation_{generation}.png"
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)  # Minimize padding in saved figure
    print(f"Saved {filename}")

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