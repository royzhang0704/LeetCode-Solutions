# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]):
        return self.preorder_traversal(root)

    def preorder_traversal(self,root):
        if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
        
        return root
