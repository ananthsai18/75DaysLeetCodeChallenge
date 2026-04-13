class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans1=float("inf")
        ans2=float("inf")
        n=len(nums)
        k=start
        for i in range(start,n):
            if nums[i]==target:
                ans1=abs(k-i)
                break
        

        for i in range(start,-1,-1):
            if nums[i]==target:
                ans2=abs(k-i)
                break
        return min(ans1,ans2)
        
        





        