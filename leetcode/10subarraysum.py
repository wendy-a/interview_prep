from typing import List

def subArrayRangesV2(nums: List[int]) -> int:
    res = 0
    inf = float('inf')
    stack = []
    min_nums = [-inf] + nums + [-inf]
    # minus sum of all minimum in the subarray
    for i, num in enumerate(min_nums):
        while stack and min_nums[stack[-1]] > num:
            idx = stack.pop()
            left = stack[-1]
            res -= min_nums[idx] * (i - idx) * (idx - left)
        stack.append(i)

    # plus sum of all maximum in the subarray
    stack = []
    max_nums = [inf] + nums + [inf]
    for i, num in enumerate(max_nums):
        while stack and max_nums[stack[-1]] < num:
            idx = stack.pop()
            left = stack[-1]
            res += max_nums[idx] * (i - idx) * (idx - left)
        stack.append(i)
    return res


def subArrayRanges(nums: List[int]) -> int:
    res = 0
    for start in range(len(nums)):
        min_num, max_num = nums[start], nums[start]
        for end in range(start, len(nums)):
            min_num = min(min_num, nums[end])
            max_num = max(max_num, nums[end])
            res += max_num - min_num
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(subArrayRangesV2([3, 1, 2, 4]))
