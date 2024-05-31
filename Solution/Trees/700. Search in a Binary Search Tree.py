 def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return None
        elif val<root.val:
            return self.searchBST(root.left,val)
        elif val>root.val:
            return self.searchBST(root.right,val)
        else:
            return root
