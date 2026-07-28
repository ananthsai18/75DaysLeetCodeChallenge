from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=s.lower()
        c=Counter(s)
        left=""
        middle=""
        for i in "abcdefghijklmnopqrstuvwxyz":
           left = left+ i*(c[i]//2)

           if c[i]%2==1:
            middle=i
        rev=left[::-1]
        return left+middle+rev

                
        