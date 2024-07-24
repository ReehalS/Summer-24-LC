// Done after learning Kotlin for my DSA class

// 124ms (97.70%), 33.30MB (98.68%)

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        if(root == null){
            return null
        }
        if(root?.left!=null || root?.right!=null){
            val left : TreeNode? = root?.left
            root?.left =  root?.right
            root?.right = left
        }
        invertTree(root?.left)
        invertTree(root?.right)
        return root
    }
}