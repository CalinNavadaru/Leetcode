class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        start = 0
        final = x - 1
        while start <= final:
            mid = (start + final) // 2
            if mid * mid <= x:
                start = mid + 1
            else:
                final = mid - 1

        return start - 1