class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        r=len(needle)
        for i in range(n-r+1):
            # print(haystack[i:i+r])
            if haystack[i:i+r]==needle:
                return i
        return -1

        