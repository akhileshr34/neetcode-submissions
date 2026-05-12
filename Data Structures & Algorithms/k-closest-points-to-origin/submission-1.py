import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        length = len(points)
        tuples = [] 
        for i in range(0, length): 
            distance = math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            tuples.append((distance, i))

        indices = [] 
        heapq.heapify(tuples)

        for j in range(0, k): 
            new = heapq.heappop(tuples) 
            indices.append(new[1])

        return [points[x] for x in indices]
