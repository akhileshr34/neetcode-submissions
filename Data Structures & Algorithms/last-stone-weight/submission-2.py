import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        
        heapq.heapify(stones)
        
        while len(stones) > 1: 
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)

            if num1 != num2: 
                heapq.heappush(stones, num1 - num2)
        
        if stones == []:
            return 0 
        return - stones[0]

            