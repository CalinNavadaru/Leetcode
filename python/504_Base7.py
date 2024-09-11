class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        n = abs(num)
        l = []
        while n:
            n, r = divmod(n, 7)
            l.append(str(r))
        if num < 0:
            l.append('-')

        return "".join(l[::-1])
