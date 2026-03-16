class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d={}
        for word in strs:
            k="".join(sorted(word))
            if k not in d:
                d[k]=[]
            d[k].append(word)
            
        print(d)
        res=[]
        for i in d:
            res.append(d[i])
        return (res)
        