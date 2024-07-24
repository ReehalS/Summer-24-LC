# 24ms (99.10%), 17.61MB (56.13%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current= head
        previous = None
        nextCell= None
        while current is not None:
            nextCell = current.next
            current.next = previous
            previous = current
            current = nextCell

        return previous
            