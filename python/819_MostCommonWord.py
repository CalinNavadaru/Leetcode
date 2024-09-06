from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r"\W+", paragraph)
        d = dict()
        s = set(banned)
        for word in words:
            word = word.lower()
            if word:
                d[word] = d.get(word, 0) + 1

        result = None
        app = 0
        for word in d:
            if word not in s and app < d[word]:
                result = word
                app = d[word]
        return result
