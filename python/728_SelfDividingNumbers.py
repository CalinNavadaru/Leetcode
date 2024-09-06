from typing import List


class Solution:

    def test(self, value):
        c = value
        while c:
            if c % 10 == 0:
                return False
            if value % (c % 10) != 0:
                return False
            c //= 10

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for v in range(left, right + 1):
            if self.test(v):
                result.append(v)

        return result
