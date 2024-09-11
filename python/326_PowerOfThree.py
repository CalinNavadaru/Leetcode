class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2 == 0 or n % 3 != 0:
            return False
        n = abs(n)
        while n % 3 == 0:
            n //= 3

        return n == 1
        # return n > 0 and (3 ** 19) % n == 0
