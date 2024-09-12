class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        mask = 0x55555555
        return n > 0 and n & (n - 1) == 0 and (n & mask) == n
        # if n <= 0:
        #     return False
        #
        # while n % 4 == 0:
        #     n //= 4
        # return n == 1
        #
        # mask = 0xAAAAAAAA
        # return n > 0 and n & (n - 1) == 0 and (n & mask) == 0
