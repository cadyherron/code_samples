"""
Given a matrix of 1s and 0s and one cell as a starting point,
    determine the greatest number of 1s that are connected to the starting cell.

Let's assume "connected" includes diagonals

m = [
0 0 0 1 1
1 0 1 0 0
1 1 1 1 1
0 0 0 0 0
1 0 1 0 1
]

cell = [2, 2]
answer = 3

cell = [0, 0]
answer = 1

cell = [4, 4]
answer = 2
"""


def connected_ones(matrix, cell):
    total_rows = len(matrix) - 1
    total_positions = len(matrix[0]) - 1
    connected = 0
    cell_row = cell[0]
    cell_position = cell[1]
    starting_row = cell_row - 1 if cell_row != 0 else cell_row
    ending_row = cell_row + 1 if cell_row != total_rows else cell_row
    starting_position = cell_position - 1 if cell_position != 0 else cell_position
    ending_position = cell_position + 1 if cell_position != total_positions else cell_position

    for row_number in range(starting_row, ending_row + 1):
        row = matrix[row_number]
        for value in row[starting_position:ending_position + 1]:
            if value == 1:
                connected += 1

    if matrix[cell_row][cell_position] == 1:
        connected -= 1

    return connected


test = [
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
