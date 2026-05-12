class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []: 
            return [[]] 
        
        ans = [] 
        more = self.subsets(nums[1:])
        for aset in more: 
            ans.append([nums[0]] + aset)
        ans += more 

        return ans 