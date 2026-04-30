class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nums=intervals
        nums.sort(key=lambda x: x[0])
        n=len(nums)
        res=[]
        s1=nums[0][0]
        e1=nums[0][1]
        for i in range(1,n):
            s2=nums[i][0]
            e2=nums[i][1]
            
            if e1>=s2:
                s1=s1
                e1=max(e1,e2)
        
            else:
                res.append([s1,e1])
                s1=s2
                e1=e2
        res.append([s1,e1])
        return res
        