class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(k):
            rev=0
            while k>0:
                r=k%10
                rev=rev*10+r
                k=k//10
            return rev

        mirror=reverse(n)
        return abs(mirror-n)
        