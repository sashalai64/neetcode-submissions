class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, cur):
            if sum(cur) == target:
                res.append(cur[:])
                return

            if i == len(nums) or sum(cur) > target:
                return
            
            cur.append(nums[i])
            backtrack(i, cur)
            cur.pop()
            backtrack(i + 1, cur)

        res = []
        backtrack(0, [])
        return res