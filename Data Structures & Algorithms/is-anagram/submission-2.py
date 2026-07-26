class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for i in t:
            if i not in h:
                return False
            h[i] -= 1
            if h[i] < 0:
                return False
        return True