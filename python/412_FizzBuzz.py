from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            value = None
            if i % 15 == 0:
                value = "FizzBuzz"
            elif i % 3 == 0:
                value = "Fizz"
            elif i % 5 == 0:
                value = "Buzz"
            else:
                value = str(i)
            result.append(value)
        return result
