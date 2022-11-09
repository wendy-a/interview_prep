from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = []
        total = 0
        self.prefixsum.append(0)
        for num in nums:
            total += num
            self.prefixsum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right + 1] - self.prefixsum[left]
