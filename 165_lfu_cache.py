from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
            
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self.get(key)
            return
            
        if len(self.key_to_val_freq) == self.capacity:
            oldest_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[oldest_key]
            
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

if __name__ == '__main__':
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))    # return 1
    lfu.put(3, 3)        # evicts key 2
    print(lfu.get(2))    # return -1 (not found)
    print(lfu.get(3))    # return 3
    lfu.put(4, 4)        # evicts key 1
    print(lfu.get(1))    # return -1 (not found)
    print(lfu.get(3))    # return 3
    print(lfu.get(4))    # return 4
