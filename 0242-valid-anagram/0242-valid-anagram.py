class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        n=len(s)
        for i in range(n):
            if s[i]!=t[i]:
                return False
        return True
        