from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        v = nums[0]
        for i in range(1, len(nums)):
            s ^= i
            v ^= nums[i]
        s ^= len(nums)
        return s ^ v