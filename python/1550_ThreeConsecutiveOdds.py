from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for elem in arr:
            if elem % 2 != 0:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                return True
        return counter == 3
