class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        ans=0
        while(l<=r):
            m=(l+r)//2
            if arr[m] < arr[m+1]:
                l=m+1
            else:
                ans=m
                r=m-1
        return (ans)
        