import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l >= r:
                return
            
            random_index = random.randint(l, r)
            nums[random_index], nums[r] = nums[r], nums[random_index]

            pivot_index = partition(l, r)
            quickSort(l, pivot_index - 1)
            quickSort(pivot_index + 1, r)


        def partition(l, r):
            p = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            
            return p
        
        quickSort(0, len(nums) - 1)
        return nums