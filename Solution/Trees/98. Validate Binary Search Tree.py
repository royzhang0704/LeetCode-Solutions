# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root)
    
    def inorder(self, current_root):
        result = []
        
        def traversal(node):
            if node.left is not None:
                traversal(node.left)
            result.append(node.val)
            if node.right is not None:
                traversal(node.right)
        
        if current_root is not None:
            traversal(current_root)
        
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:  # 考慮到相等的情況
                return False
        return True

        
