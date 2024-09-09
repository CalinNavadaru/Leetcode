from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            for i in range(n):
                result[j][i] = matrix[i][j]

        return result
