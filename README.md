# Conway's Game of Life - Matrix-Vector Sparse Implementation

## Overview

This project implements Conway's Game of Life using matrix-vector operations and sparse matrices. The simulation custom operations along with sparse matrix representations (CSR format) to update the state of the grid over a series of generations.

## Features

- **Matrix Operations:** Reads an initial grid from a text file (`init.txt`), vectorizes it, and constructs a sparse neighbor matrix in CSR format.
- **Simulation:** Runs 25 generations of Conway's Game of Life, updating the state based on neighbor counts.
- **Visualization:** Uses matplotlib to display each generation with a brief pause between updates.
- **Output:** Saves the final state to `final_state.txt`.

## Requirements

- Python 3.x
- Required Python packages:
  - `matplotlib`

You can install the required packages using pip:

```bash
pip install matplotlib 
```
File Structure

    main.py:
    Contains the main entry point. The main() function invokes the simulation, initializes the grid from init.txt, updates the grid for each generation, and displays the results.

    conway_backend.py:
    Handles the simulation logic by reading the initial state, building the sparse neighbor matrix, and updating the grid state for each generation.

    conway_frontend.py:
    Contains functions for visualizing the grid (displaying the current generation) and saving the final state to a text file.

    matrix_operations.py:
    Implements all matrix and vector operations, including functions for reading a matrix from file, vectorization, matrix multiplication (both standard and sparse/CSR-based), and building the neighbor matrix.

    init.txt:
    Contains the initial grid configuration. This file should be present in the same folder as the Python scripts. An example for a 5x5 grid might look like:

    0 1 1 0 0
    0 1 1 0 0
    0 0 0 0 1
    1 0 0 1 1
    1 1 0 0 0

How to Use

    Ensure all required files are in one folder:
    Make sure main.py, conway_backend.py, conway_frontend.py, matrix_operations.py, and init.txt are located in the same directory.

    Prepare your init.txt file:
    Edit or create an init.txt file with the desired initial grid. Each row should contain space-separated values (0 for dead, 1 for alive).

    Run the Program:
    Execute the main program by running main.py. This will automatically invoke the main() function:

    python main.py

    The simulation will run for 25 generations, displaying each generation in a matplotlib window. After the simulation, the final grid state is saved in final_state.txt.

Citation & Authorship

    Authors:
    Faycal Kilali
        Contributions include all code modules and documentation.

    AI Assistance:
    Portions of the code and documentation were generated with the help of Claude.AI.

    Project Version:
    1.0

Additional Notes

    The code is designed to run in a single folder without requiring additional directories or external files.
    For further details about the mathematical modeling and matrix operations used in this project, please refer to the accompanying documentation or inline code comments.

