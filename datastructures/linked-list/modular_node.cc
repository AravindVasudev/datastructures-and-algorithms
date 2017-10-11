#include <iostream>
#include <vector>

struct Node {
    int data;
    Node *next;
};

Node* array_to_list(std::vector<int> arr) {
    Node *head = new Node;
    Node *ptr = head;
    int size = arr.size();
    for (int i = 0; i < size; i++) {
        ptr->data = arr[i];
        ptr->next = (i == size - 1 ? NULL : new Node);
        ptr = ptr->next;
    }

    return head;
}

std::string visualize(Node *head) {
    std::string visualized_list = "";

    if (head == NULL) return "";
    if (!head->next) return std::to_string(head->data);
    while (head) {
        visualized_list += std::to_string(head->data) + " -> ";
        head = head->next;
    }

    return visualized_list + "NULL";
}

int modular_node(Node *head, int k) {
    Node *ptr;
    int i = 1;
    if (!head) return -1;
    while (head) {
        if (i++ % k == 0) ptr = head;
        head = head->next;
    }

    return ptr->data;
}

int main() {
    std::vector<int> arr = {2, 5, 6, 1, 9, 10, 45};
    Node *list = array_to_list(arr);

    std::cout << visualize(list) << "\n" << modular_node(list, 4) << "\n";

    return 0;
}