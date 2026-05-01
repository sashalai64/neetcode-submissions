class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        res = 0

        for n in nums:
            cur = 0
            if n - 1 not in nums:
                while n in nums:
                    cur += 1
                    n += 1   
            res = max(res, cur)
        
        return res