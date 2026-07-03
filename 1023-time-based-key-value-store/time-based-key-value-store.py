import bisect
class TimeMap:

    def __init__(self):
        self.key_d = {}
        self.val_d = {}
        self.key_time = {} #dic with sorted list
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_d[timestamp] = key
        self.val_d[timestamp] = value
        
        if key in self.key_time:
            self.key_time[key].append(timestamp)
        else:
            self.key_time[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        #check exact match
        if timestamp in self.key_d:
            if self.key_d[timestamp]== key: #check if it is same key
                return self.val_d[timestamp]
        #find nearest timestamp for key
        if key in self.key_time:
            time_list = self.key_time[key]
            nearest = bisect.bisect_right(time_list,timestamp)
            if nearest == 0 :
                return ""
            else:
                return self.val_d[time_list[nearest-1]]
        else:
            return ""
 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)