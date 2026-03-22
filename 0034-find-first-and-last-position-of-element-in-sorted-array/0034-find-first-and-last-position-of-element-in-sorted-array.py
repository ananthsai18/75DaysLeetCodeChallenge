class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sm=-1
        n=len(nums)
        r= n-1
        l=0
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                sm= m
                r=m-1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
                
        lm=-1
        n=len(nums)
        r= n-1
        l=0
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                lm=m
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return [sm,lm]
        