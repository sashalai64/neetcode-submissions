class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur, pick):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                if pick[i] == False:
                    pick[i] = True
                    cur.append(nums[i])
                    backtrack(cur, pick)
                    cur.pop()
                    pick[i] = False

        
        res = []
        backtrack([], [False] * len(nums))

        return res