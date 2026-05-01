class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = sorted(count.items(), key = lambda x: x[1], reverse = True)
        maxCount = freq[0][1] - 1
        slots = maxCount * n

        for char, val in freq[1:]:
            slots -= min(maxCount, val)
        
        return len(tasks) + slots if slots > 0 else len(tasks)