class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return [newInterval]
        i=0
        s1=intervals[i][0]

        m=newInterval[0]
        if m<=s1:
            intervals.insert(0,newInterval)
        p=2
        for j in range(n):
            s2=intervals[j][0]
            if s1<=m and m<=s2:
                intervals.insert(j,newInterval)
                p=0
                break
            i+=1

        if p==2:
            intervals.append(newInterval)
        print(intervals)

        res=[]

        s1=intervals[0][0]
        e1=intervals[0][1]
        k=len(intervals)
        for i in range(k):
            s2=intervals[i][0]
            e2=intervals[i][1]
            
            if e1>=s2:
                s1=s1
                e1=max(e1,e2)
                continue
            else:
                res.append([s1,e1])
                s1=s2
                e1=e2
        res.append([s1,e1])
        return res 
        