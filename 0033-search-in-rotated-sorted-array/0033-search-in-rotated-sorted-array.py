class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        mini=0
        while(l<=r):
            m=(l+r)//2
            if nums[m]<=nums[n-1]:
                mini=m
                r=m-1
            else:
                l=m+1


        l=0
        r=mini
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1

        l=mini
        r=n-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return -1  