import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         tracker = collections.defaultdict(int)
#         for x in s:
#             tracker[x] += 1
#         for c in t:
#             tracker[c] -= 1
#         return all(c == 0 for c in tracker.values())