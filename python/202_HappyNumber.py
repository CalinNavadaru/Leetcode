class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while n != 1:
            c = n
            n = 0
            while c:
                n += (c % 10) ** 2
                c //= 10
            if n in d:
                return False
            d.add(n)

        return True
