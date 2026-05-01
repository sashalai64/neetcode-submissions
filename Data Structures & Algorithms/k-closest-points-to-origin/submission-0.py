class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            dis = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-dis, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            dis, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res