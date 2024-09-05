from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        value = sum(x for x in rolls)
        remaining = total - value
        if 6 * n < remaining or remaining < n:
            return []
        s = 6 * n
        q, r = divmod(s - remaining, n)
        result = [6 - q] * n
        for i in range(r):
            result[i] -= 1

        return result