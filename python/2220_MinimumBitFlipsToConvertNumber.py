class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        while start or goal:
            if (start & 1) != (goal & 1):
                result += 1
            start >>= 1
            goal >>= 1

        return result