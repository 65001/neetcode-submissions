# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sameTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if left and right:
            return left.val == right.val and self.sameTree(left.left, right.left) and self.sameTree(left.right, right.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root and subRoot:
            return (root.val == subRoot.val and self.sameTree(root, subRoot)) or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        return False