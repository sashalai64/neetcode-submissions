class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)

        for key, val in count.items():
            heapq.heappush(heap, [val, key])

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for val, key in heap:
            res.append(key)
        
        return res