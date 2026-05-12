class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []: 
            return [[]] 
        
        ans = [] 
        for ind, num in enumerate(nums): 
            nextp = self.permute(nums[:ind] + nums[ind+1:]) 
            if nextp == [[]]: 
                ans += [[num]]
                continue 
            
            for p in nextp: 
                p.append(num)
                ans.append(p)

        return ans
         