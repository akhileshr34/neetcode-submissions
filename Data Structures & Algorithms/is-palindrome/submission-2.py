class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1 
        
        while r > l: 
            if not s[r].isalnum(): 
                r -= 1 
                continue 
            if not s[l].isalnum(): 
                l += 1
                continue 

            if s[l] != s[r]: 
                if s[l].isalpha() and s[r].isalpha(): 
                    if ord(s[l]) + 32 != ord(s[r]) and ord(s[r]) + 32 != ord(s[l]):
                        return False
                else:
                    return False
            l += 1 
            r -= 1  
        return True  