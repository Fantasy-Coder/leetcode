from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #记录最大直径
        ans = 0
        #定义一个函数，返回以当前节点为根节点的树的最大深度
        def dfs(node:Optional[TreeNode]) -> int:
            #如果当前节点为空，则返回-1
            if node is None:
                return -1
            #计算左子树和右子树的最大深度
            l_len = dfs(node.left) + 1
            r_len = dfs(node.right) + 1
            #更新最大直径 nonlocal 关键字用于在函数内部修改外部作用域中的变量
            nonlocal ans
            #更新最大直径
            ans = max(ans, l_len + r_len)
            #返回以当前节点为根节点的树的最大深度
            return max(l_len, r_len)

        dfs(root)
        return ans