# 295. Find Median from Data Stream
# The median is the middle value in an ordered integer list.

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -self.small[0])
        heapq.heappop(self.small)
        
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())
    mf.add_num(3)
    print(mf.find_median())
