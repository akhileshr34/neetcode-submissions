import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        ans = []

        l = 0
        
        for r in range(len(nums)):
            heapq.heappush(maxheap, (-nums[r], r))
            
            while maxheap[0][1] < l:
                heapq.heappop(maxheap)

            if r >= k - 1:
                ans.append(-maxheap[0][0])
                l += 1

        return ans