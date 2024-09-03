from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(2, numRows):
            result.append([1])
            prev = result[-2]
            for j in range(len(result[-2]) - 1):
                result[-1].append(prev[j] + prev[j + 1])
            result[-1].append(1)

        return result