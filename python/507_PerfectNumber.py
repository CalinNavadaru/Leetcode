from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        q = int(sqrt(num))
        for i in range(2, q + 1):
            if num % i == 0:
                s += (i + num // i)

        if q * q == num:
            s += q
        return s == num
