#include <iostream>
#include <vector>

struct Node {
    int data;
    Node *next;
};

Node* array_to_list(std::vector<int> arr) {
    Node *new_head = new Node;
    Node *ptr = new_head;
    for (int i = 0; i < arr.size(); i++) {
        ptr->data = arr[i];
        ptr->next = (i == arr.size() - 1 ? NULL : new Node);
        ptr = ptr->next;
    }

    return new_head;
}

std::string visualize(Node *head) {
    std::string visualized_list = "";

    if (head == NULL) return "";
    if (!head->next) {
        return std::to_string(head->data);
    }

    while (head->next) {
        visualized_list += std::to_string(head->data) + " -> ";
        head = head->next;
    }

    return visualized_list + std::to_string(head->data);
}

Node* pair_reverse(Node *head) {
    if (!head || !head->next) return NULL;

    Node *next = head->next;
    head->next = next->next;
    next->next = head;
    head = next;

    head->next->next = pair_reverse(head->next->next);
    return head;
}

int main() {
    std::vector<int> arr = {1, 2, 1, 3, 4, 8};
    Node *list = array_to_list(arr);

    std::cout << visualize(list) << "\n" << visualize(pair_reverse(list)) << std::endl;
}