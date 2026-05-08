from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counter = defaultdict(int)
        check = defaultdict(int)

        for char in t:
            counter[char] += 1

        l = 0
        ans = ""

        for r in range(len(s)):
            check[s[r]] += 1

            works = True

            for char in counter:
                if check[char] < counter[char]:
                    works = False
                    break

            while works:
                if ans == "" or (r - l + 1) < len(ans):
                    ans = s[l:r+1]

                check[s[l]] -= 1
                l += 1

                for char in counter:
                    if check[char] < counter[char]:
                        works = False
                        break

        return ans