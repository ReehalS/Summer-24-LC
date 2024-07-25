# There are 2 solutions for this.
# Solution #1 uses actual binary calculations to add the numbers.
# Solution #2 uses python built-in functions to add the numbers, but I personally think it's 'cheating'.

# Solution #1
# 33ms (83.10%), 16.61MB (21.01%)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        if(lenA>lenB):      # normalize length for both strings
            b = ("0"*(lenA-lenB)) + b   
        elif(lenB>lenA):
            a = ("0"*(lenB-lenA)) + a
            lenA = lenB
        carry = False
        resultString=""
        # binary add with carry
        for i in range(lenA-1,-1,-1):
            if a[i] =="1" and b[i] =='1':
                if carry:
                    resultString += '1'
                else:
                    resultString += '0'
                carry = True
            elif a[i]== "1" or b[i] == "1":
                if carry:
                    resultString += '0'
                    carry = True
                else:
                    resultString += '1'
            else:
                if carry:
                    resultString += "1"
                    carry = False
                else:
                    resultString += "0"

        if carry:
            resultString += "1"
        reversedString = resultString[::-1]
        return reversedString

# Solution #2, using string conversion functions
# 29ms (94.48%), 16.53MB (51.59%)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intA = int(a,2)
        intB = int(b,2)
        return "{0:b}".format(intA+intB)
    

# Solution #2, but a single line of code
# 29ms (94.48%), 16.25MB (97.32%)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a,2)+int(b,2))

