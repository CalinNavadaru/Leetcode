class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v = s.rsplit(maxsplit=1)[-1]
        return len(v)
