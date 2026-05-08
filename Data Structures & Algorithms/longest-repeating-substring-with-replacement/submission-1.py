from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        amount = defaultdict(int)
        maxfreq = 0 
        l = 0 
        r = 0 
        ans = 0 

        while r < length: 
            amount[s[r]] += 1 

            maxfreq = max(maxfreq, amount[s[r]])

            while (r - l + 1) - maxfreq > k:
                amount[s[l]] -= 1 
                l += 1 
            
            ans = max(ans, r - l + 1)
            r += 1 
        
        return ans

        