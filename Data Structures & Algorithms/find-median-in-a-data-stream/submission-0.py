class MedianFinder:

    def __init__(self):
        self.even = True 
        self.lower = [] 
        self.higher = []

    def addNum(self, num: int) -> None:
        if self.higher == []: 
            heapq.heappush(self.higher, num)
            self.even = False 
            return 
        
        if self.even: 
            if num < - self.lower[0]: 
                med = - heapq.heappop(self.lower)
                heapq.heappush(self.lower, - num)
                heapq.heappush(self.higher, med)
            else: 
                heapq.heappush(self.higher, num)
            self.even = False 
            return 
    
        if num > self.higher[0]: 
            transfer = - heapq.heappop(self.higher)
            heapq.heappush(self.lower, transfer)
            heapq.heappush(self.higher, num)
        else: 
            heapq.heappush(self.lower, - num)
        self.even = True 
        return


    def findMedian(self) -> float:
        if self.even: 
            return (((- self.lower[0]) + self.higher[0]) / 2)
        return self.higher[0]

        