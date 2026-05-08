class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        vals = self.dic[key]
        time_idx = self.search(vals, timestamp)
        return vals[time_idx][0] if time_idx >= 0 else ""

    
    def search(self, vals, timestamp):
        l, r = 0, len(vals) - 1

        while l <= r:
            mid = (l + r) // 2

            # rightmost valid time <= timestamp
            if vals[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return r





