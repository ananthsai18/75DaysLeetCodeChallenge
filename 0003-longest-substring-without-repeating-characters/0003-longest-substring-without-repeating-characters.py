class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        temp=set()
        maxi=float("-inf")
        i=0
        n=len(s)
        for j in range(n):

            if s[j] in temp:
                while s[j] in temp:
                    temp.remove(s[i])
                    i+=1
                temp.add(s[j])
            else:
                temp.add(s[j])

            print(temp)
            maxi=max(maxi,j-i+1)

        return maxi

         
            
        