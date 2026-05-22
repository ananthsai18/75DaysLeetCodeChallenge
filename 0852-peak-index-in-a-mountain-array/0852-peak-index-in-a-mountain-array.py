class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        n=len(arr)
        h=n-1
        res=-2
        while(l<=h):
            m=(l+h)//2
            if arr[m]<arr[m+1]:
                l=m+1
            else:
                res=m
                h=m-1
        return res
