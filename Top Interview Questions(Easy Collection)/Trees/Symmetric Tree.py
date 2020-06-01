Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 

Follow up: Solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.ismirror(root.left,root.right)
    
    def ismirror(self,left,right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            if left.val==right.val:
                return  self.ismirror(left.left,right.right) and self.ismirror(left.right,right.left)             
        return False
            
            
    # def ismirror(self,left,right):
    #     if left and right:
    #             return (left.val==right.val and self.ismirror(left.left,right.right) and self.ismirror(left.right,right.left))              
    #     return left==right
