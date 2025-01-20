from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()
        self.capacity = capacity

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.dic:
            val = self.dic[key]
            del self.dic[key]  # Remove the key
            self.dic[key] = val  # move to back   
        else:
            val =  -1
        return val

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            del self.dic[key] 
        if len(self.dic) == self.capacity:
            #need to evitr
            self.dic.popitem(last=False)
        self.dic[key] = value

   
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)