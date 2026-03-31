from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#栈
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        strck = []
        ans = []
        cur = root

        while cur or strck:
            while cur:
                strck.append(cur)
                cur = cur.left
            cur = strck.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
#递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node:Optional[TreeNode]) ->None:
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        
        ans = []
        dfs(root)
        return ans