from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        new = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            new[i // n][i % n] = original[i]

        return new
