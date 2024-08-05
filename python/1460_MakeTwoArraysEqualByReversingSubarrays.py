from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for e1, e2 in zip(target, arr):
            d[e1] = d.get(e1, 0) + 1
            d[e2] = d.get(e2, 0) - 1

        return all(d[k] == 0 for k in d)
