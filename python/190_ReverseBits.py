class Solution:
    def reverseBits(self, n: int) -> int:
        # s = 0
        # t = 0
        # n = str(bin(n)[2:])
        # n = '0' * (32 - len(n)) + n
        # for c in n:
        #     if c == '1':
        #         s += 2 ** t
        #     t += 1
        # return s
        result = 0
        for _ in range(32):
            result = (result << 1) + (n & 1)
            n = n >> 1
        return result