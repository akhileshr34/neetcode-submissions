class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = [0] * 26
        check = [0] * 26

        l = 0
        r = len(s1) - 1

        for char in s1:
            counter[ord(char) - ord('a')] += 1

        for ind in range(l, r + 1):
            check[ord(s2[ind]) - ord('a')] += 1

        while r < len(s2):
            if counter == check:
                return True

            if r == len(s2) - 1:
                break

            check[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1
            check[ord(s2[r]) - ord('a')] += 1

        return False