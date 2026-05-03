class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canditate=0
        c=0

        for i in nums:
            if c==0:
                canditate=i
                c+=1
            elif i==canditate:
                c+=1
            else:
                c-=1
        return canditate

        