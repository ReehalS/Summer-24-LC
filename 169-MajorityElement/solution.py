
# my solution

# 167ms (72.79%), 17.90 (87.89%) 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        if(len(nums)<=2):
            return nums[0]
        for n in nums:
            if n in d:
                d[n] +=1
                if(d[n]>len(nums)//2):
                    return n
            else:
                d[n] = 1

            
        