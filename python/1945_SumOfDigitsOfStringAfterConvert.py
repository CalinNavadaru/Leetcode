class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = int("".join([str(ord(x) - ord('a') + 1) for x in s]))
        while k:
            new_number = 0
            while number:
                number, digit = divmod(number, 10)
                new_number += digit

            number = new_number
            k -= 1

        return number
