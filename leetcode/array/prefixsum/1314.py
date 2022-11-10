from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        presum = self.getpresum(mat)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # left top cornor
                x1 = max(i - k, 0)
                y1 = max(j - k, 0)
                # right bottom cornor
                x2 = min(i + k, m - 1)
                y2 = min(j + k, n - 1)
                res[i][j] = self.sumregion(presum, x1, y1, x2, y2)
        return res

    def getpresum(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] + mat[i - 1][j - 1] - presum[i - 1][j - 1]
        return presum

    def sumregion(self, presum: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> int:
        return presum[x2 + 1][y2 + 1] - presum[x1][y2 + 1] - presum[x2 + 1][y1] + presum[x1][y1]
