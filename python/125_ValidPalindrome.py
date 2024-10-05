def is_alphanumeric(c):
    return c in "1234567890" or ord('a') <= ord(c.lower()) <= ord('z')


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     left = 0
    #     right = len(s) - 1
    #     while left <= right:
    #         if not is_alphanumeric(s[left]):
    #             left += 1
    #         elif not is_alphanumeric(s[right]):
    #             right -= 1

    #         elif s[left].lower() == s[right].lower():
    #             left += 1
    #             right -= 1

    #         else:
    #             return False

    #     return True
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s) // 2))
