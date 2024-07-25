
# 409ms (80.70%), 31.89MB (74.97%)

# using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for l in nums:
            if l in s:
                return True
            s.add(l)
        return False