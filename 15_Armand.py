import numpy as np

grid_length = 20
grid = np.ones((grid_length + 1, grid_length + 1))
for i in range(1, grid_length + 1):
    for j in range(1, grid_length + 1):
        paths = 0
        grid[i][j] = grid[i-1][j] + grid[i][j-1]
print(grid[grid_length][grid_length])
