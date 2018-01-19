#include <iostream>
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

int size(Node *root) {
    if (!root) return 0;
    return size(root->left) + size(root->right) + 1;
}

int size_without_recursion(Node *root) {
    int size = 0;
    std::queue<Node*> q;

    if (!root) return size;

    q.push(root);
    while (!q.empty()) {
        Node *cur = q.front(); q.pop();

        if (cur->left)  q.push(cur->left);
        if (cur->right) q.push(cur->right);

        size++;
    }
    return size;
}

int main() {
    Node *root = new Node(1);

    root->left  = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(4);
    root->left->right = new Node(3);

    std::cout << size(root) << size_without_recursion(root);
    return 0;
}
