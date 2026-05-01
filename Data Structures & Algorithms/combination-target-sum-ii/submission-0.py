class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, temp, target):
            if target == 0:
                res.append(temp[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                
                temp.append(candidates[i])
                dfs(i + 1, temp, target - candidates[i])
                temp.pop()
        
        res = []
        candidates.sort()
        dfs(0, [], target)

        return res