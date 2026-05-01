class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            # if right part is sorted, min is mid or to the left
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1
        
        return nums[l]