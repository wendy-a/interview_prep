from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    res = [[]]
    path = []
    n = len(nums)

    def dfs(idx):
        path.append(nums[idx])
        res.append(list(path))
        for nexti in range(idx+1, n):
            dfs(nexti)
        path.pop()
        return

    for i in range(n):
        dfs(i)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(subset([1, 2, 3]))
