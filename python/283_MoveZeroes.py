from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        v = 0
        for index, elem in enumerate(nums):
            if elem == 0:
                v += 1
            else:
                nums[index - v] = nums[index]
        for index in range(len(nums) - v, len(nums)):
            nums[index] = 0
        # v = 0
        # for index, elem in enumerate(nums):
        #     if elem == 0:
        #         v += 1
        #     else:
        #         aux = nums[index]
        #         nums[index] = nums[index - v]
        #         nums[index - v] = aux
