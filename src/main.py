"""
Author: Faycal Kilali
Citation: ChatGPT (OpenAI, 2025) for assistance with main().
Version: 1.0
"""

import conway_backend
import conway_frontend
import matrix_operations
import matplotlib.pyplot as plt


def main():
    """
    Main entry to program. Begins the game of Conways.
    AI Critique: the AI failed to invoke some functions from matrix_operations and assumed they existed within the same document.
    I also had to change the name of the function 'update_conways' to 'time_step' in accordance with conway_backend.py function header.
    """
    # Set up the plot window once
    plt.figure(figsize=(8, 8))

    # Number of generations to simulate
    generations = 25

    # Initialize Conway's Game of Life
    X, x, (values, col_index, row_ptr) = conway_backend.initialize_conways()

    # Display initial state (Generation 0)
    conway_frontend.display(X, generation=0, pause_time=2.0)


    # Run simulation for specified number of generations
    for generation in range(1, generations + 1):
        # Update state using CSR matrix multiplication
        x = conway_backend.time_step(x, values, col_index, row_ptr)

        # Convert vector back to 2D matrix for display
        X = matrix_operations.matrixify(x)

        # Display current state
        conway_frontend.display(X, generation=generation, pause_time=2.0)

    # Save final state to output file
    conway_frontend.save_final_state(X)

    # Keep the figure open until manually closed
    plt.show()


# Forces the main function above to be the main function when called by the terminal
if __name__ == "__main__":
    main()