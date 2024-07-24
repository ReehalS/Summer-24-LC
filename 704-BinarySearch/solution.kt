// Done after learning Kotlin for my DSA class

// 236ms (75.25%), 39.57MB (33.28%)


class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size-1
        
        while(left<= right){
            if(nums[left] == target){
                return left
            }
            if(nums[right] == target){
                return right
            }
            val mid = left+ (right-left)/2
            if(nums[mid] == target){
                return mid
            }
            if(nums[mid]<target){
                left = mid+1
            }
            else{
                right = mid-1
            }
        }

        return -1
    }
}
