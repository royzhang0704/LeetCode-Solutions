class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.inorder(root,result)
        return result


    def inorder(self,root,result):
        if root is None:
            return 
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)


“”“
time:O(n) 每個node都訪問一次 
space:O(n) 二元樹可以為skew 複雜度取決於遞迴深度即樹的高度 worst case:(n) 
”“”
