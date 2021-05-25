"""
    Approach 1: Using OrderedDict
"""
from collections import OrderedDict
class LRUCache(OrderedDict):
    
    def __init__(self, capacity: int):
        # Initialize OD with given capacity
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If given key not found in dict, return -1
        if key not in self:
            return -1
        else:
            # Else we move the key, value to the end
            # and return the value
            self.move_to_end(key)
            return self[key]

    def put(self, key: int, value: int) -> None:
        # If the key is already present, move it to the end
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        
        # Once the OD gets larger than the given capacity,
        # we prune it and evict the oldest unused item
        # from the beginning of the OD
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)