class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()
            backtrack(i + 1, cur)

        res = []
        backtrack(0, [])
        return res