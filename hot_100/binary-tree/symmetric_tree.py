from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #递归 函数定义
        def recur(L,R):
            #如果都为空则是对称的
            if not L and not R:
                return True
            #如果有一个为空或者左右数值不一致则不是对称的
            if not L or not R or L.val != R.val:
                return False
            #除上述两种情况外，判断左子树的左节点与右子树的右节点，左子树的右节点和右子树的左节点 进行递归
            return recur(L.left, R.right) and recur(L.right, R.left)
        #如果root为空直接返回对称。如果不为空则开始递归
        return not root or recur(root.left,root.right)