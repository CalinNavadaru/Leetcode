class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        v = x ^ y
        c = 0
        for i in range(31):
            if v & (1 << i):
                c += 1
        return c