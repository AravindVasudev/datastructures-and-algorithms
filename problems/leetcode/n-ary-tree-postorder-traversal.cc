// https://leetcode.com/problems/n-ary-tree-postorder-traversal/
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        return postorder(root, result);
    }

private:
    vector<int> postorder(Node* root, vector<int>& result) {
        if (!root) {
            return result;
        }

        for (auto child : root->children) {
            postorder(child, result);
        }

        result.push_back(root->val);
        return result;
    }
};
