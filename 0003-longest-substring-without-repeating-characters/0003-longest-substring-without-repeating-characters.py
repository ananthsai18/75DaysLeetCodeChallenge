class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        temp=""
        maxi=float("-inf")
        i=0
        n=len(s)
        for j in range(n):

            if s[j] in temp:
                while s[j] in temp:
                    temp=temp[1:]
                    i+=1
                temp+=s[j]
            else:
                temp+=s[j]

            print(temp)
            maxi=max(maxi,j-i+1)

        return maxi

         
            
        