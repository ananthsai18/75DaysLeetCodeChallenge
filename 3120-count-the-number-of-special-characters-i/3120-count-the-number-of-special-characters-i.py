class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a=set()
        b=set()
        for i in word:
            if i.isupper():
                a.add(i.lower())
            else:
                b.add(i)
        c=0
        for i in a:
            if i in b:
                c+=1
        return c

        