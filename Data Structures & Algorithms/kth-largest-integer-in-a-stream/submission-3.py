import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort() 
 
        self.num = k 
        self.larger = nums[-k:]
        heapq.heapify(self.larger)

    def add(self, val: int) -> int: 
        if len(self.larger) < self.num: 
            heapq.heappush(self.larger, val)
        elif val > self.larger[0]: 
            heapq.heappop(self.larger)
            heapq.heappush(self.larger, val)
        return self.larger[0]
        

