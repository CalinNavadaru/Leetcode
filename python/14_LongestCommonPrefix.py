from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = [x for x in strs[0]]
        for s in strs:
            index = -1
            for i in range(min(len(prefix), len(s))):
                if prefix[i] != s[i]:
                    index = i
                    break
            if len(s) < len(prefix):
                prefix = prefix[:len(s)]
            if index != -1:
                prefix = prefix[:index]

        return "".join(prefix)
