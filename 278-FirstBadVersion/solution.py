# 34ms (59.94%), 16.60MB (8.74)

# could optimize instead of using a recursive binary search.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n//2
        if(n==1): 
            return 1

        #print(mid)
        if(isBadVersion(mid)):
            #print("mid bad")
            badVersion = self.checkBad(1, mid)
        else:
            badVersion = self.checkBad(mid,n)

        return badVersion
    
    def checkBad(self, lower:int, upper:int) -> int:
        mid = lower+((upper-lower)//2)
        #print("Upper:"+str(upper)+". Mid: "+str(mid)+". Lower: "+ str(lower))
        if(upper==lower):
            return lower
        elif(isBadVersion(mid)):
            #print("mid bad")
            badVersion = self.checkBad(lower, mid)
        else:
            #print("mid not bad")
            badVersion = self.checkBad(mid+1,upper)
        return badVersion