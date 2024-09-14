from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        s = 1
        for el in nums:
            if s == el:
                s += 1
        for el in nums:
            if s == el:
                s += 1
        return s
