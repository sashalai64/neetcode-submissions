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

        res = 0
        n = len(nums)
        dfs(0, 0)
        
        return res