class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum, maxNum = 1, 1
        res = max(nums)

        for n in nums:
            temp = maxNum
            maxNum = max(n, maxNum * n, minNum * n)
            minNum = min(n, temp * n, minNum * n)

            res = max(res, maxNum)
        
        return res