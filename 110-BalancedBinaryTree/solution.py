# 30ms (99.46%), 17.59MB (72.12%)
# 
# 
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(self.height(root) >=0):
            return True
        else:
            return False
        
    def height(self,root: Optional[TreeNode] ) -> int:
        if not root:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if(leftHeight<0) or (rightHeight<0) or abs(leftHeight-rightHeight) >1:
            return -1
        maximum = max(leftHeight, rightHeight)
        return maximum+1