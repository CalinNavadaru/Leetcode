from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        c = 0
        for i in range(31):
            zero = 0
            one = 0
            for j in range(len(nums)):
                if (nums[j] >> i) & 1:
                    one += 1
                else:
                    zero += 1
            c += zero * one

        return c


print(Solution().totalHammingDistance([4, 14, 2]))
print(Solution().totalHammingDistance([4, 14, 4]))
