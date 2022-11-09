from collections import deque
from typing import List


def orangesRotting(self, grid: List[List[int]]) -> int:
    def isvalid(grid, row, col):
        return (0 <= row < rows) and \
               (0 <= col < cols) and \
               (grid[row][col] == 1)

    # use bfs
    # initialize queue, count fresh orange and add rotten into queue
    queue = deque()
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            if grid[r][c] == 1:
                fresh += 1

    if len(queue) == 0:  # no rotten
        return -1 if fresh > 0 else 0

    minute = 0
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                newr, newc = row + x, col + y
                if isvalid(grid, newr, newc):
                    grid[newr][newc] = 2
                    fresh -= 1
                    queue.append((newr, newc))

        if queue:  # finish first iteration
            minute += 1
    return minute if fresh == 0 else -1
