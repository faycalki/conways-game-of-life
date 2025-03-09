"""
Author: Faycal Kilali
Project: Conway's Game of Life
Citation: ChatGPT (OpenAI, 2025) for assistance with time_step function
Version: 1.0
"""

import matrix_operations

def initialize_conways():
    """
    Initializes Conways by reading the input file and constructing a 2D grid from it as a full matrix, then vectorizing the matrix.
    Afterwards, builds the initial sparse matrix A in COO form, then converts it to CSR form.
    AI Critique: attempted to convert the neighbor matrix A to COO form, but the neighbor_matrix function already generates it in COO form. Thus, I eliminated that aspect.
    :return: X the grid matrix, x the vectorized grid, (values, col_index, row_ptr) the CSR form of the neighbor matrix A.
    """

    # Assign X to be the matrix acquired from init.txt.
    X = matrix_operations.read_matrix("init.txt")

    # Convert matrix to vectorized form, assign as x.
    x = matrix_operations.vectorize(X)

    # First, build the neighbor matrix A in COO format
    rows, cols, data  = matrix_operations.build_neighbor_matrix(X)

    # Convert to CSR
    values, col_index, row_ptr = matrix_operations.compressed_sparse_row_format(rows, cols, data)

    # Return the result
    return X, x, (values, col_index, row_ptr)


def time_step(x, values, col_index, row_ptr):
    """
    Updates Conway's Game of Life grid based on the rules.
    AI Critique: no issues.

    :param x: current state vector
    :param values: CSR values array
    :param col_index: CSR column indices array
    :param row_ptr: CSR row pointers array
    :return: new state vector
    """
    # Calculate neighbor counts using CSR matrix multiplication
    neighbor_counts = matrix_operations.matrix_multiply_csr(values, col_index, row_ptr, x)

    # Construct new grid with appropriate size to fill later
    new_x = [0] * len(x)

    # Apply Conway's Game of Life rules
    for i in range(len(x)):
        if x[i] == 1:  # Cell is alive
            if neighbor_counts[i] < 2 or neighbor_counts[i] > 3:
                new_x[i] = 0  # Cell dies
            else:
                new_x[i] = 1  # Cell survives
        else:  # Cell is dead
            if neighbor_counts[i] == 3:
                new_x[i] = 1  # Cell becomes alive
            else:
                new_x[i] = 0  # Cell stays dead

    return new_x


