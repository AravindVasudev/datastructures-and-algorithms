#include <iostream>
#include <queue>
#include <stack>

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

void inorder_nonrecursive(Node *root) {
    if (!root) return;

    Node *cur = root;
    std::stack<Node*> s;
    bool done = false;

    while (!done) {
        if (cur) {
            s.push(cur);
            cur = cur->left;
        } else {
            if (!s.empty()) {
                cur = s.top();
                s.pop();

                std::cout << cur->data;
                cur = cur->right;
            } else {
                done = true;
            }
        }
    }
}

void preorder_nonrecursive(Node *root) {
    if (!root) return;

    Node *cur = root;
    std::stack<Node*> s;
    bool done = false;

    while (!done) {
        if (cur) {
            std::cout << cur->data;

            s.push(cur);
            cur = cur->left;
        } else {
            if (!s.empty()) {
                cur = s.top()->right;
                s.pop();
            } else {
                done = true;
            }
        }
    }
}

void preorder_nonrecursive_2(Node *root) {
    if (!root) return;

    std::stack<Node*> s;
    s.push(root);

    while(!s.empty()) {
        Node *temp = s.top();
        s.pop();

        std::cout << temp->data;
        if (temp->right) s.push(temp->right);
        if (temp->left)  s.push(temp->left);
    }
}

void postorder_nonrecursive(Node *root) {
    if (!root) return;

    Node *cur = root;
    std::stack<Node*> s;
    std::stack<int> op;

    s.push(root);
    while (!s.empty()) {
        Node *cur = s.top();
        s.pop();

        if (cur->left)  s.push(cur->left);
        if (cur->right) s.push(cur->right);

        op.push(cur->data);
    }

    while (!op.empty()) {
        std::cout << op.top();
        op.pop();
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
    std::cout << "\n";
    inorder_nonrecursive(root);
    std::cout << "\n";
    preorder_nonrecursive(root);
    std::cout << "\n";
    preorder_nonrecursive_2(root);
    std::cout << "\n";
    postorder_nonrecursive(root);


    return 0;
}
