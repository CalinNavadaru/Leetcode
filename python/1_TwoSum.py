from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, elem in enumerate(nums):
            value = d.get(target - elem, -1)
            if value != -1:
                return [value, index]
            else:
                d[elem] = index
