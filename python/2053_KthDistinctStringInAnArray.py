from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = dict()
        for e in arr:
            d[e] = d.get(e, 0) + 1
        c = 0
        for e in d:
            if d[e] == 1:
                c += 1
            if c == k:
                return e
        return ""
