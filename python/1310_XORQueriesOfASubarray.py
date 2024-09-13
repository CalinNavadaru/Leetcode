from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        for index in range(1, len(arr)):
            arr[index] = arr[index - 1] ^ arr[index]

        for query in queries:
            if query[0] == 0:
                result.append(arr[query[1]])
            else:
                result.append(arr[query[1]] ^ (arr[query[0] - 1]))

        return result
#
# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         XorS = []
#         s = 0
#         result = []
#         for elem in arr:
#             s ^= elem
#             XorS.append(s)
#
#         for query in queries:
#             if query[0] == query[1]:
#                 result.append(arr[query[0]])
#             elif query[0] == 0:
#                 result.append(XorS[query[1]])
#             else:
#                 result.append(XorS[query[1]] ^ (XorS[query[0] - 1]))
#
#         return result