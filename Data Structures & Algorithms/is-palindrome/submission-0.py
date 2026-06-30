class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            c1 = s[p1].lower()
            c2 = s[p2].lower()
            if not c1.isalnum():
                p1 += 1
                continue
            if not c2.isalnum():
                p2 -= 1
                continue
            if c1 != c2:
                return False
            p1 += 1
            p2 -= 1
        return True