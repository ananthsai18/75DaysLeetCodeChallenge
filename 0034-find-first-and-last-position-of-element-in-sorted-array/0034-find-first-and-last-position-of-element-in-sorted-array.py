class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def calc(nums,target,isStart):
            ans=-1
            n=len(nums)
            r= n-1
            l=0
            while(l<=r):
                m=(l+r)//2
                if nums[m]==target:
                    ans=m
                    if isStart:
                        r=m-1
                    else:
                        l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return ans

        a=calc(nums,target,True)
        b=calc(nums,target,False)  
        return [a,b]
        