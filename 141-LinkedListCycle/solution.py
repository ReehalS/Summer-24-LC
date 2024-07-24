# https://leetcode.com/problems/linked-list-cycle/

# 49ms (32.40%), 19.51MB (10.94%)

# Might redo later

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
            
        return False