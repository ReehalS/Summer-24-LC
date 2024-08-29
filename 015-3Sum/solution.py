#v2  643ms (79.13%), 20.60MB (83.75%)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # v2 
        nums.sort()
        answer=[]
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]
            left=i+1
            right=len(nums)-1
            while(right>left):
                sums = curr+nums[left]+nums[right]         
                if(sums > 0):
                    right-=1
                elif(sums < 0):
                    left+=1
                else:
                    answer.append([curr,nums[left],nums[right]])
                    left+=1
                    while(nums[left]==nums[left-1] and left<right):
                        left+=1
        return answer


        # v1, O(n3) , times out for large inputs
        # answer=[]
        # for i in range(0,len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if(nums[i]+nums[j]+nums[k]==0):
        #                 points = [nums[i],nums[j],nums[k]]
        #                 points.sort()
        #                 if(points not in answer):
        #                     answer.append(points)
        # return answer