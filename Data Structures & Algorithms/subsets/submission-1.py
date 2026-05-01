class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, cur):
            if i == n:
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)
        
        n = len(nums)
        res = []
        dfs(0, [])

        return res