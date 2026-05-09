class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1 

        while True: # there is always one valid solution 
            computed = numbers[l] + numbers[r]

            if computed == target: 
                return [l + 1, r + 1]
            elif computed < target: 
                l += 1 
            else: 
                r -= 1 