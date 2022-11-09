def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
    # 2 round dfs.
    # 1 round for pacific
    # 1 round for atlantic
    # go through the map again. find both

    totalrow = len(grid)
    totalcol = len(grid[0])
    # 0 not flow. 1 pacific flow 2 atlantic flow. 3 both flow
    visited = [[[] for _ in range(totalcol)] for _ in range(totalrow)]

    def isvalid(grid, row, col, ocean):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and (not ocean in visited[row][col])

    def dfs(grid, row, col, ocean):
        if not isvalid(grid, row, col, ocean):
            return

        visited[row][col].append(ocean)
        curr = grid[row][col]
        # 4 direction
        if isvalid(grid, row + 1, col, ocean) and grid[row + 1][col] >= curr:
            dfs(grid, row + 1, col, ocean)

        if isvalid(grid, row - 1, col, ocean) and grid[row - 1][col] >= curr:
            dfs(grid, row - 1, col, ocean)

        if isvalid(grid, row, col + 1, ocean) and grid[row][col + 1] >= curr:
            dfs(grid, row, col + 1, ocean)

        if isvalid(grid, row, col - 1, ocean) and grid[row][col - 1] >= curr:
            dfs(grid, row, col - 1, ocean)

    # top pacific and bottom atlantic
    for col in range(totalcol):
        dfs(grid, 0, col, 1)
        dfs(grid, totalrow - 1, col, 2)
    # left pacific and. right atlantic
    for row in range(totalrow):
        dfs(grid, row, 0, 1)
        dfs(grid, row, totalcol - 1, 2)

    res = []
    for row in range(totalrow):
        for col in range(totalcol):
            if len(visited[row][col]) == 2:
                res.append([row, col])
    return res