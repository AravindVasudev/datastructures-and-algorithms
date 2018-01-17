#include <iostream>
#include <queue>

struct Node {
    int data;
    Node *left, *right;
};

void preorder(Node *root) {
    if (!root) return;

    std::cout << root->data;
    preorder(root->left);
    preorder(root->right);
}

void inorder(Node *root) {
    if (!root) return;

    inorder(root->left);
    std::cout << root->data;
    inorder(root->right);
}

void postorder(Node *root) {
    if (!root) return;

    postorder(root->left);
    postorder(root->right);
    std::cout << root->data;
}

void levelorder(Node *root) {
    if (!root) return;

    std::queue<Node*> q;

    q.push(root);
    while (!q.empty()) {
        Node *cur = q.front(); q.pop();

        std::cout << cur->data;
        if (cur->left)  q.push(cur->left);
        if (cur->right) q.push(cur->right);
    }
}

int main() {
    Node *root = new Node{1, NULL, NULL};

    root->left  = new Node{2, NULL, NULL};
    root->right = new Node{3, NULL, NULL};

    root->left->left  = new Node{4, NULL, NULL};
    root->left->right = new Node{5, NULL, NULL};

    preorder(root);
    std::cout << "\n";
    inorder(root);
    std::cout << "\n";
    postorder(root);
    std::cout << "\n";
    levelorder(root);


    return 0;
}
