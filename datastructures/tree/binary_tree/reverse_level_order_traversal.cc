#include <iostream>
#include <queue>
#include <stack>

struct Node {
    int data;
    Node *left, *right;

    Node(int data) {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};

void reverse_level_order_traversal(Node *root) {
    std::queue<Node*> q;
    std::stack<Node*> stack;

    if (!root) return;

    q.push(root);
    while (!q.empty()) {
        Node *cur = q.front(); q.pop();

        if (cur->left)  q.push(cur->left);
        if (cur->right) q.push(cur->right);

        stack.push(cur);
    }

    while (!stack.empty()) {
        std::cout << stack.top()->data;
        stack.pop();
    }
}

int main() {
    Node *root = new Node(1);

    root->left  = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(4);
    root->left->right = new Node(3);

    reverse_level_order_traversal(root);
    return 0;
}
