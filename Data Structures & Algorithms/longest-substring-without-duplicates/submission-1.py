from collections import defaultdict 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(bool)

        length = len(s)
        maxlen = 0 
        curr = ""

        for i in range(0, length): 
            if not seen[s[i]]: 
                curr += s[i]
                seen[s[i]] = True 
            else: 
                char = s[i]
                maxlen = max(maxlen, len(curr))
                prev = curr.find(char)

                for j in range(0, prev): 
                    seen[curr[j]] = False 
                
                curr = curr[prev+1:] + char
        
        return max(maxlen, len(curr))
            