class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):
            nonlocal res

            if i == n:
                if total == target:
                    res += 1
                return
            
            dfs(i + 1, total + nums[i])
            dfs(i + 1, total - nums[i])

        n = len(nums)
        res = 0
        dfs(0, 0)

        return res