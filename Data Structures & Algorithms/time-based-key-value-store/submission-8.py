import bisect

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        new = (value, timestamp)
        self.data.setdefault(key, []).append(new)

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.data.keys():
            return ans

        arr = self.data[key]
        pos = bisect.bisect_left(arr, timestamp, key=lambda x: x[1])
        if pos == len(arr) or (pos < len(arr) and arr[pos - 1][1] <= timestamp and arr[pos][1] > timestamp):
            ans = arr[pos - 1][0]
        elif (pos < len(arr) and arr[pos][1] <= timestamp):
            ans = arr[pos][0]
        return ans