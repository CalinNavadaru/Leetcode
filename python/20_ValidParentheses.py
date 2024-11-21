class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack[-1]
                if not (last == '(' and char == ')' or last == '[' and char == ']' or last == '{' and char == '}'):
                    return False
                stack.pop()

        return len(stack) == 0
