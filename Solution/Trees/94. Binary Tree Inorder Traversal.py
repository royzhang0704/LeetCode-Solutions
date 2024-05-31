class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
       vector<int> result;
       if(root==nullptr){
           return result;
       }
       vector<int> left=inorderTraversal(root->left);
       result.insert(result.end(),left.begin(),left.end());
       result.push_back(root->val);
       vector<int> right=inorderTraversal(root->right);
       result.insert(result.end(),right.begin(),right.end());
       return result;
    }
};
