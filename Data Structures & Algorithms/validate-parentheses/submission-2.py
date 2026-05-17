class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for char in s: 
            if char == '(': 
                stack.append(')')
            elif char == '[': 
                stack.append(']')
            elif char == '{': 
                stack.append('}')
            else: 
                if stack == [] or stack.pop() != char: 
                    return False 
    
        if len(stack) > 0: return False 
        return True