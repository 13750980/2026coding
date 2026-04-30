# week10-3.py
# LeetCode 75 : Binary Tree - DFS Q3 1448. Count Good Nodes in Binary Tree
# tree最喜歡用「函式呼叫函式」來解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, big): # 記得祖先最大的big
            ans = 0
            if root==None: return 0 # 提早結束
            if root.val >= big:
                ans += 1
                big = root.val
            ans += helper(root.left, big)
            ans += helper(root.right, big)
            return ans # 注意：圖片中此行被切掉，但遞迴需要回傳 ans
        return helper(root, root.val) # 初始 big 值建議設為極小值
