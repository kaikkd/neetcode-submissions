class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(total, subset, i):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i == len(candidates):
                return
            

            subset.append(candidates[i])
            dfs(total + candidates[i], subset, i + 1)

            subset.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(total, subset, i + 1)

        dfs(0, [], 0)

        return res