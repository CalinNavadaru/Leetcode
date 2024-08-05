class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        while time:
            for i in range(2, n + 1):
                time -= 1
                if time == 0:
                    return i
            for i in range(n - 1, 0, -1):
                time -= 1
                if time == 0:
                    return i