class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n=len(firstList)
        m=len(secondList)
        i=0
        j=0
        res=[]

        while((i<n) and (j<m)):
            s1=firstList[i][0]
            e1=firstList[i][1]

            s2=secondList[j][0]
            e2=secondList[j][1]

            if s1 <= s2 :
                if(e1>=s2):
                    p=max(s1,s2)
                    q=min(e1,e2)
                    res.append([p,q])
            
            elif s1 > s2 :
                if (e2>=s1):
                    p=max(s1,s2)
                    q=min(e1,e2)
                    res.append([p,q])
            
            if e1<=e2:
                i+=1
            else:
                j+=1
        return res

        