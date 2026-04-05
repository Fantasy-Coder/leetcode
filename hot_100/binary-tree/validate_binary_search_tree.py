from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#前序遍历
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #定义函数，记录当前节点和最大值与最小值
        def helper(node, min_val, max_val):
            if not node:
                return True
            # 核心判断：节点必须在合法范围内
            if node.val <= min_val or node.val >= max_val:
                return False
            # 递归左右子树，自带范围约束（自带子节点判断，无需重复检查）
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
        
        return helper(root, float('-inf'), float('inf'))
#中序遍历
class Solution:
    pre = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)