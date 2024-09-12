from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        result = 0
        for word in words:
            if all(c in allowed_chars for c in word):
                result += 1

        return result
        # allowed_letters = 0
        # for letter in allowed:
        #     allowed_letters += (1 << (ord(letter) - ord('a')))
        #
        # counter = 0
        # for word in words:
        #     is_consistent = True
        #     for c in word:
        #         is_allowed = allowed_letters >> (ord(c) - ord('a')) & 1
        #
        #         if not is_allowed:
        #             is_consistent = False
        #             break
        #
        #     if is_consistent:
        #         counter += 1
        #
        # return counter