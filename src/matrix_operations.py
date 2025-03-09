"""
Author: Faycal Kilali
Project: Conway's Game of Life
Version: 1.0
Citation: ChatGPT (OpenAI, 2025) and Claude.AI (Anthropic, 2025) for Neighbor_Matrix.
"""

MATRIX_ROWS = 0
MATRIX_COLS = 0

def read_matrix(file):
    """
    Reads a matrix from a file, ignoring leading/trailing whitespace and empty lines. Each line is split into integers and stored as a list of lists.
    :param file: Path to the input file containing the matrix with space-separated values.
    :return: A 2D list representing the matrix.
    """
    global MATRIX_ROWS, MATRIX_COLS

    with open(file, 'r') as f:
        matrix = [list(map(int, line.split())) for line in f if line.strip()]

    MATRIX_ROWS, MATRIX_COLS = len(matrix), len(matrix[0]) # Set the matrix rows and columns expected
    return matrix

def matrixify(array):
    """
    Given a 1D array consisting of 64 integers, constructs the corresponding 8x8 matrix in row-major order.
    :param matrix: array of 64 integers
    :return: the matrix representation as a 2D array.
    """
    matrix = [[0 for _ in range(MATRIX_COLS)] for _ in range(MATRIX_ROWS)] # Construct 2D matrix

    # Construct matrix from vectorized form to matrix form
    row = 0
    for col in range (0, len(array)):
        curr_element = array[col]

        # If column is divisible by MATRIX_COLS and not equal to 0, then that means we must move to the next row.
        if col % MATRIX_COLS == 0 and col != 0:
            row += 1

        # Fill matrix with element at appropriate position
        matrix[row][col % MATRIX_COLS] = curr_element

    return matrix

def vectorize(matrix):
    """
    Given a matrix of the form of a 2D array (two dimensional array), vectorizes it in row-major order.
    :param matrix: the matrix to be vectorized
    :return:  the vectorized matrix
    """
    vectorized = [0] * (MATRIX_COLS * MATRIX_ROWS)

    curr_index = 0
    for row in range (0, len(matrix)):
        for col in range (0, len(matrix[0])):
            curr_element = matrix[row][col]
            vectorized[curr_index] = curr_element
            curr_index += 1
    return vectorized



def compressed_sparse_row_format(rows, cols, data):
    """
    Converts a matrix from Coordinate List (COO) format to Compressed Sparse Row (CSR) format.

    :param rows: List of row indices of nonzero elements.
    :param cols: List of column indices of nonzero elements.
    :param data: List of nonzero values.

    :return: (values, col_index, row_ptr) - CSR representation of the matrix.
    """

    # Initialize arrarys for CSR as cols
    values = []
    col_index = []

    # Determine maximum number of rows
    num_rows = max(rows) + 1 if rows else 0

    # Initialize row pointers
    row_ptr = [0] * (num_rows + 1)

    # Construct the CSR, using zip to simultaneously perform those iterations.
    for r, c, v in zip(rows, cols, data):
        values.append(v)  # Add the value to values
        col_index.append(c)  # Add the column index
        row_ptr[r + 1] += 1  # Count nonzero entries for the row

    # Add up the counts to a sum for each row poiinter that shares the same rows
    for i in range(1, len(row_ptr)):
        row_ptr[i] += row_ptr[i - 1]

    return values, col_index, row_ptr


def build_neighbor_matrix(matrix):
    """
    Builds a matrix representing the number of neighbors for each cell in Conway's Game of Life.

    :param matrix: 2D matrix representing the current state of the game (1 for alive, 0 for dead)
    :return: rows, cols, data lists representing the neighbor matrix in COO format
    """
    # Initialize lists for COO format
    rows = []
    cols = []
    data = []

    # Get dimensions
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Define the 8 possible directions to check for neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top left, top, top right
        (0, -1), (0, 1),  # Left, right
        (1, -1), (1, 0), (1, 1)  # Bottom left, bottom, bottom right
    ]

    # For each cell in the matrix
    for row in range(num_rows):
        for col in range(num_cols):
            # Calculate the linear index of this cell
            cell_index = row * num_cols + col

            # For each direction
            for d_row, d_col in directions:
                neighbor_row = row + d_row
                neighbor_col = col + d_col

                # Ensure the neighbor is within bounds
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    # Calculate the linear index of the neighbor
                    neighbor_index = neighbor_row * num_cols + neighbor_col

                    # Add this relationship to the COO format
                    rows.append(cell_index)
                    cols.append(neighbor_index)
                    data.append(1)  # Weight of 1 for each neighbor

    return rows, cols, data


def matrix_multiply_csr(values, col_index, row_ptr, x):
    """
    Performs matrix-vector multiplication using CSR format.

    :param values: array of non-zero values
    :param col_index: array of column indices
    :param row_ptr: array of row pointers
    :param x: vector to multiply with
    :return: result vector
    """

    # Number of rows in the result
    num_rows = len(row_ptr) - 1

    # Create result vector with same length as input vector
    result = [0] * len(x)

    # Multiplication that handles dimension mismatch
    for i in range(num_rows):
        if i >= len(result):
            print(f"  Warning: Row {i} exceeds result vector length {len(result)}")
            break

        for j in range(row_ptr[i], row_ptr[i + 1]):
            if j >= len(col_index):
                print(f"  Warning: Column index {j} exceeds col_index length {len(col_index)}")
                continue

            col = col_index[j]
            if col >= len(x):
                print(f"  Warning: Column {col} exceeds input vector length {len(x)}")
                continue

            result[i] += values[j] * x[col]

    return result




