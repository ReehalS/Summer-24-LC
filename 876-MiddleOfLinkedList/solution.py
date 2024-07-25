# iterative

# 33ms (71.42%), 16.48MB (51.40%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        single = head
        while head:
            head = head.next
            if head:
                head = head.next
                single = single.next
        return single