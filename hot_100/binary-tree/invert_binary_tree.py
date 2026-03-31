from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#递归
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
#栈
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        #将根节点入栈 
        stack = [root]
        #当栈不为空时，弹出栈顶节点
        while stack:
            node = stack.pop() 
            #如果左右子树不为空，将左右子树入栈
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            #交换左右子树
            node.left, node.right = node.right, node.left
        return root