# 2 different solutions, one mine, one's idea is from the solutions


# original code, my own solution

# 37ms (56.40%), 16.65MB (13%)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for l in s:
            if l in d:
                c = d[l]
                d[l]= c+1
            else:
                d[l] = 1
        center = False
        length = 0
        for l in d:
            if(d[l]%2 == 0):
                length+=d[l]
            elif(d[l]%2 == 1) and not center:
                length+=d[l]
                center = True
            elif(d[l]%2 ==1) and center:
                length+=d[l]-1
        return length
    

# new idea from solutions, only read the explanation, code is mine

# 35ms (71.22%), 16.46MB (89.43%)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = set()
        length = 0
        for l in s:
            if l in d:
                d.remove(l)
                length+=2
            else:
                d.add(l)
            
        if d:
            length+=1

        return length