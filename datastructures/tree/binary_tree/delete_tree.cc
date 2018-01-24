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

void delete_tree(Node *root) {
    if (!root) return;

    delete_tree(root->left);
    delete_tree(root->right);
    delete root;
}

int main() {
    Node *root = new Node(1);

    root->left  = new Node(2);
    root->right = new Node(5);
    root->left->left = new Node(4);
    root->left->right = new Node(3);

    delete_tree(root);

    std::cout << (root == NULL);
    return 0;
}
