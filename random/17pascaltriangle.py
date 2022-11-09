from typing import List


# random 2221
def triangularSum(nums: List[int]) -> int:
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            nums[j] = (nums[j] + nums[j + 1]) % 10
    return nums[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(triangularSum([2, 7, 4, 3]))
