# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        min_length = min(n // 2, m // 2)
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        for q in range(min_length):
            for j in range(q, n - q):
                if not head:
                    return matrix
                value = head.val
                head = head.next
                matrix[q][j] = value

            for i in range(q + 1, m - q):
                if not head:
                    return matrix
                value = head.val
                head = head.next
                matrix[i][n - q - 1] = value

            for j in range(n - q - 2, q - 1, -1):
                if not head:
                    return matrix
                value = head.val
                head = head.next
                matrix[m - q - 1][j] = value

            for i in range(m - q - 2, q, -1):
                if not head:
                    return matrix
                value = head.val
                head = head.next
                matrix[i][q] = value

        for j in range(min_length, n - min_length):
            if not head:
                return matrix
            value = head.val
            head = head.next
            matrix[min_length][j] = value

        for i in range(min_length + 1, m - min_length):
            if not head:
                return matrix
            value = head.val
            head = head.next
            matrix[i][n - min_length - 1] = value

        return matrix

# class Solution:
#     def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
#         result = [[-1 for _ in range(n)] for _ in range(m)]
#         x, y = 0, 0
#         curr_direction = 0
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         while head:
#             result[x][y] = head.val
#             head = head.next
#
#             nx = x + directions[curr_direction][0]
#             ny = y + directions[curr_direction][1]
#
#             if not (0 <= nx < m and 0 <= ny < n and result[nx][ny] == -1):
#                 curr_direction = (curr_direction + 1) % 4
#
#             x, y = x + directions[curr_direction][0], y + directions[curr_direction][1]
#
#         return result


print(a := Solution().spiralMatrix(1, 4, ListNode(0, ListNode(1, ListNode(2)))))
print(3)
