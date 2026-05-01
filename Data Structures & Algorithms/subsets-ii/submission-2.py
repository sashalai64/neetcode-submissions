class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)


        n = len(nums)
        nums.sort()
        res = []
        dfs(0, [])

        return res
