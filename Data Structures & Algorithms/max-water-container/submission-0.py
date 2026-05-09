class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        marea = 0 
        curr = 0 

        while l < r: 
            curr = min(heights[l], heights[r]) * (r - l)
            marea = max(curr, marea)

            if heights[l] < heights[r]: 
                l += 1 
            else: 
                r -= 1

        return marea 
            