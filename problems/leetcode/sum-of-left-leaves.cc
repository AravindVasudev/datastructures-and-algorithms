// https://leetcode.com/problems/sum-of-left-leaves/
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root, bool isLeft = false) {
        if (!root) {
            return 0;
        }

        if (!root->left && !root->right) {
            return isLeft ? root->val : 0;
        }

        return sumOfLeftLeaves(root->left, true) + sumOfLeftLeaves(root->right, false);
    }
};
