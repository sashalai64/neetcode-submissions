class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):
            if i == n:
                if total == target:
                    return 1
                else:
                    return 0

            if (i, total) in cache:
                return cache[(i, total)]

            ways = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            cache[(i, total)] = ways
            
            return ways

        n = len(nums)
        cache = {}

        return dfs(0, 0)
        