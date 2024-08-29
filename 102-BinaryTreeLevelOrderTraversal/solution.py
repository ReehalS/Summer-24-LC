# 29ms (97.98%), 17.00 (94.14%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=[root]
        while queue:
            children=[]
            for i in range(len(queue)):
                child = queue.pop(0)
                if(child):  #keep adding children to the queue
                    children.append(child.val)
                    queue.append(child.left)
                    queue.append(child.right)
            if(children):
                res.append(children)
            
        return res