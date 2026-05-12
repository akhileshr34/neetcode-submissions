class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': 
            return []
        
        if digits == '2': 
            return ['a', 'b', 'c']
        elif digits == '3': 
            return ['d', 'e', 'f']
        elif digits == '4': 
            return ['g', 'h', 'i']
        elif digits == '5': 
            return ['j', 'k', 'l']
        elif digits == '6': 
            return ['m', 'n', 'o']
        elif digits == '7': 
            return ['p', 'q', 'r', 's']
        elif digits == '8': 
            return ['t', 'u', 'v']
        elif digits == '9': 
            return ['w', 'y', 'x', 'z']

        ans = [] 
        first = self.letterCombinations(digits[0])
        nex = self.letterCombinations(digits[1:])
        for combo in nex: 
            for char in first: 
                char += combo 
                ans.append(char)
        
        return ans