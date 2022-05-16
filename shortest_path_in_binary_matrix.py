def shortest_path_binary_matrix(grid) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    row = len(grid)
    column = len(grid[0])
    if grid[0][0] or grid[-1][-1]:
        # start and end must be 0
        return -1
    if row == 1 and grid[0][0] == 0:
        # single cell
        return 1

    queue = [(0, 0)]
    visited = {(0, 0)}
    step = 1

    while len(queue):
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for dx, dy in directions:  # apply our directions to this point
                nx = x + dx
                ny = y + dy
                # check if this point is in our matrix: 0 <= nx < row and 0 <= ny < column
                # check if this point is 0: grid[nx][ny] == 0
                # check if we've already visited this point: (nx, ny) not in visited
                if 0 <= nx < row and 0 <= ny < column and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if nx == row - 1 and ny == column - 1:
                        return step + 1
        step += 1
    return -1
