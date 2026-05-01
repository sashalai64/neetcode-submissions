class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # {key: [(time1, val1), (time2, val2)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or self.timeMap[key][0][0] > timestamp:
            return ""
        
        idx = self.binary_search(key, timestamp)
        return self.timeMap[key][idx][1]

    def binary_search(self, key, timestamp):
        arr = self.timeMap[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            # last value <= timestamp
            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return r
