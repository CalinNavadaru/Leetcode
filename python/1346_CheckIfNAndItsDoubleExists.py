from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for index, element in enumerate(arr):
            if ((element % 2 == 0 and d.get(element // 2, None))
                    or d.get(element * 2, None)):
                return True
            d[element] = 1

        return False