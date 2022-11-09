from typing import List


def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def isvalid(grid, row, col):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and (grid[row][col] == 1)

    def dfs(grid, row, col):
        # base case
        if not isvalid(grid, row, col):
            return 0

        # mark visited
        grid[row][col] = 0

        up = dfs(grid, row - 1, col)
        down = dfs(grid, row + 1, col)
        left = dfs(grid, row, col - 1)
        right = dfs(grid, row, col + 1)

        return up + down + left + right + 1

    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:  # find a island
                area = dfs(grid, row, col)
                max_area = max(max_area, area)
    return max_area