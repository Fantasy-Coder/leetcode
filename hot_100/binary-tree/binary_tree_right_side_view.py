from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        #定义dfs
        def dfs(node:Optional[TreeNode], depth:int) -> None:
            if node is None:
                return
            #如果深度与ans长度一致，加入该节点的值
            if  depth == len(ans):
                ans.append(node.val)
            #遍历右、左节点
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        cur = [root]
        #如果cur存在则进入循环
        while cur:
            #将cur中最后的节点值加入（即某一深度的最右侧节点）
            ans.append(cur[-1].val)
            nxt = []
            #将下一深度的节点加入nxt
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            #在cur循环完后，加入下一深度的节点
            cur = nxt
        return ans
