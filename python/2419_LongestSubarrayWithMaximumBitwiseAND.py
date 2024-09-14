from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # length = 1
        # max_value = nums[0]
        # max_length = 1
        # value = nums[0]
        # for i in range(1, len(nums)):
        #     value = value & nums[i]
        #     length += 1
        #     if not (value >= max_value and value >= nums[i]):
        #         length = 1
        #         value = nums[i]
        #
        #     if value > max_value or (value == max_value and length > max_length):
        #         max_length = length
        #         max_value = value
        #
        # return max_length
        m, c, result = 0, 0, 0
        for e in nums:
            if e > m:
                m = e
                c = 0
                result = c

            if e == m:
                c += 1
            else:
                c = 0

            result = max(result, c)

        return result
