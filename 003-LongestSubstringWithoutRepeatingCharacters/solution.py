# 53ms (68.55%), 16.63MB (39.98%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        curmax= 0
        maximum=0
        while(right<len(s)):
            for i in range(left,right):
                if(s[right]==s[i]):
                   left=i+1
                   break
            right+=1
            curmax=right-left
            maximum=max(curmax, maximum)
        return maximum