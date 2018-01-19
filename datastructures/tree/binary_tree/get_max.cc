#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>

struct Node {
    int data;
    Node *left, *right;

    Node(int data) {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};

int get_max(Node *root) {
    int root_val, left, right, maxi = INT_MIN;

    if (root == NULL) return maxi;

    root_val = root->data;
    left     = get_max(root->left);
    right    = get_max(root->right);

    return std::max(root_val, std::max(left, right));
}

int get_max_without_recursion(Node *root) {
    int maxi = INT_MIN;
    std::queue<Node*> q;

    if(!root) return maxi;

    q.push(root);
    while (!q.empty()) {
        Node *cur = q.front(); q.pop();

        maxi = std::max(maxi, cur->data);

        if (cur->left)  q.push(cur->left);
        if (cur->right) q.push(cur->right);
    }

    return maxi;
}

int main() {
    Node *root = new Node(1);

    root->left  = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(4);
    root->left->right = new Node(3);

    std::cout << get_max(root) << get_max_without_recursion(root);
    return 0;
}
