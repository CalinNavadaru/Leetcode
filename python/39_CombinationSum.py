from typing import List


class Solution:
    results = []
    solution = []
    s = 0

    def __generateSolutions(self, candidates: List[int], target: int, start: int):
        if Solution.s == target:
            Solution.results.append(Solution.solution.copy())
            return
        for i in range(start, len(candidates)):
            Solution.solution.append(candidates[i])
            Solution.s += candidates[i]
            if Solution.s <= target:
                self.__generateSolutions(candidates, target, i)
            Solution.s -= Solution.solution.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Solution.results = []
        Solution.solution = []
        Solution.s = 0
        candidates.sort()
        if candidates[0] > target:
            return Solution.results
        self.__generateSolutions(candidates, target, 0)
        return Solution.results