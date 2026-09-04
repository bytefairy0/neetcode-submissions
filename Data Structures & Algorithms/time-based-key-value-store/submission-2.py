class TimeMap:

    def __init__(self):
        # dict of lists of dict
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        if self.timeMap.get(key):
            self.timeMap[key].append(pair)
        else:
            self.timeMap[key] = [pair]

    def get(self, key: str, timestamp: int) -> str:
        # binary search on timestamps
        if not self.timeMap.get(key):
            return ""

        l = len(self.timeMap[key])
        s, e = 0, l-1
        ans = ""
        while s <= e:
            mid = s + (e-s)//2

            if self.timeMap[key][mid][0] <= timestamp:
                ans =  self.timeMap[key][mid][1]
                s = mid+1
            else:
                e =  mid-1

        return ans

        
        

