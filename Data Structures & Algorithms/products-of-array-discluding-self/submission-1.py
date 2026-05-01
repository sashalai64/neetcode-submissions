class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n

        for i in range(n-1):
            pre[i+1] = pre[i] * nums[i]
        
        post = 1
        for i in range(n-2, -1, -1):
            post *= nums[i+1]
            pre[i] = pre[i] * post
        
        return pre