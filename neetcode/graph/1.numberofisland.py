from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def isvalid(grid, row, col):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and (grid[row][col] == '1')


    def dfs(grid, row, col):
        # base case
        if not isvalid(grid,row,col):
            return

        # action in the node
        grid[row][col] = '0'

        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row, col - 1)

    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                dfs(grid, row, col)
                res += 1
    return res