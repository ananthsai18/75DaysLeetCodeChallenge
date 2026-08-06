class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            p=1
            while(n>0):
                r=n%10
                p*=r
                n=n//10
            return p
        
        bool =True
        i=n
        while bool:
            k=product(i)
            if(k%t==0):
                bool=False
                return i
            else:
                i=i+1
        