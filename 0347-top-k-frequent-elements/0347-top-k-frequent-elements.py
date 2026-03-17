class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=nums
        d=Counter(n)
        s=dict(sorted(d.items(),key =lambda item:item[1],reverse=True))
        c=0
        ans=[]
        for i in s:
            if c==k:
                break
            ans.append(i)
            c+=1
        return ans