class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, cur, pick):
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for i in range(n):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    dfs(i + 1, cur, pick)
                    cur.pop()
                    pick[i] = False

        n = len(nums)
        res = []
        pick = [False] * n
        dfs(0, [], pick)

        return res