from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0 for _ in code]
        if k == 0:
            return result
        elif k < 0:
            code = code[::-1]
            c_k = -k
        else:
            c_k = k
        for index, value in enumerate(code):
            for i in range(index + 1, index + c_k + 1):
                result[index] += code[i % len(code)]

        return result if k > 0 else result[::-1]
        