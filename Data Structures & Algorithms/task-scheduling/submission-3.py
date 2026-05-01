class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # O(T)
        freq = sorted(count.items(), key = lambda x: x[1], reverse = True) # O(UlogU)
        maxCount = freq[0][1] - 1
        slots = maxCount * n

        # O(U)
        for char, val in freq[1:]:
            slots -= min(maxCount, val)
        
        return len(tasks) + slots if slots > 0 else len(tasks)