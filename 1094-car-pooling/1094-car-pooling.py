class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[]
        for i,j,k in trips:
            arr.append([j,i])
            arr.append([k,-i])

        arr.sort(key=lambda x:(x[0],x[1]))
        print(arr)
        c=0
        for i,j in arr:
            c+=j
            
            if c>capacity:
                return False
        
        return True
