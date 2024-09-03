from typing import List


class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     transport = 0
    #     transport, digits[-1] = divmod(digits[-1] + 1 + transport, 10)
    #     for i in range(len(digits) - 2, -1, -1):
    #         transport, digits[i] = divmod(digits[i] + transport, 10)
    #
    #     if transport:
    #         digits.insert(0, transport)
    #
    #     return digits
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits