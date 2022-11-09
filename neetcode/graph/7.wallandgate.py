from collections import deque
from typing import List


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    def isvalid(row, col):
        return (0 <= row < rows) and \
               (0 <= col < cols) and \
               (rooms[row][col] == 2147483647)

    queue = deque()
    rows = len(rooms)
    cols = len(rooms[0])

    # initialize the queue
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                queue.append((i, j))

    # return if no gate in rooms
    if not queue:
        return

    step = 0
    while queue:
        # go through the list
        step += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + x, c + y
                if isvalid(new_r, new_c):
                    rooms[new_r][new_c] = step
                    queue.append((new_r, new_c))