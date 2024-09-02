from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int):
        s = sum(x for x in chalk)
        k = k % s
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
