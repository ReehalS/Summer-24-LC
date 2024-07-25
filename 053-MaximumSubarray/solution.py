# This solution was taught in ECS 122A (Algorithm Design and Analysis) by Professor Z. Bai at UC Davis in Spring Quarter 2024.
# Uses Divide and Conquer to solve the problem of maximum subarray

# Time complexity: O(n*log(n))

# 1195ms (5.04%), 31.09MB (28.24%)
# upon submission I realized this was terrible for actual speed and memory usage
# This solution is very slightly altered from Professor Bai's solution as the low and high indices were not needed for the final solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)-1
        total = self.maxSubArrayHelper(nums,0,length)
        return total

    def maxSubArrayHelper(self,nums: List[int], low:int,high:int) -> int:
        if high==low:
            return nums[low]
        else:
            mid = (low+high)//2
            leftSum = self.maxSubArrayHelper(nums,low,mid)
            rightSum = self.maxSubArrayHelper(nums,mid+1,high)
            xSum = self.maxXingSubArray(nums,low,mid,high)

            if (leftSum>= rightSum) and (leftSum>=xSum):
                return leftSum
            elif (rightSum>=leftSum) and (rightSum >=xSum):
                return rightSum
            else:
                return xSum
            
    def maxXingSubArray(self,nums:List[int], low:int,mid:int,high:int)-> int:
        leftSum = float('-inf')
        Sum = 0
        maxLeft=0
        for i in range(mid,low-1,-1):
            Sum= Sum+ nums[i]
            if Sum>=leftSum:
                leftSum = Sum
                maxLeft = i
        
        rightSum = float('-inf')
        Sum = 0
        maxRight=0
        for j in range(mid+1,high+1):
            Sum = Sum+nums[j]
            if Sum>=rightSum:
                rightSum=Sum
                maxRight = j

        total = leftSum+rightSum
        return total

# Alternate solution with O(n) time complexity

# todo