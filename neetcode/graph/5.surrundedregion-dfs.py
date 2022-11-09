from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    maxrow = len(board)
    maxcol = len(board[0])
    visited = [[0 for _ in range(maxcol)] for _ in range(maxrow)]

    def isvalid(row, col):
        return (0 <= row < maxrow) and \
               (0 <= col < maxcol) and \
               (board[row][col] == "O") and \
               (visited[row][col] == 0)

    def dfs(row, col):
        if not isvalid(row, col):
            return

        visited[row][col] = 1

        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            dfs(row + x, col + y)

    # scan left and right bound
    for row in range(maxrow):
        if board[row][0] == "O":
            dfs(board, row, 0)
        if board[row][maxcol - 1] == "O":
            dfs(row, maxcol - 1)

    # scan top and bottom bound
    for col in range(maxcol):
        if board[0][col] == "O":
            dfs(0, col)
        if board[maxrow - 1][col] == "O":
            dfs(maxrow - 1, col)

    # update value
    for i in range(maxrow):
        for j in range(maxcol):
            if board[i][j] == "O" and visited[i][j] == 0:
                board[i][j] = "X"
