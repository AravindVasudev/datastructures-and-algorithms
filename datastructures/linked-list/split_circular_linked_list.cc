#include <iostream>
#include <vector>

struct Node {
    int data;
    Node *next;
};

Node* array_to_clist(std::vector<int> arr) {
    Node *new_head = new Node;
    Node *ptr = new_head;
    for (int i = 0; i < arr.size(); i++) {
        ptr->data = arr[i];
        ptr->next = (i == arr.size() - 1 ? new_head : new Node);
        ptr = ptr->next;
    }

    return new_head;
}

Node* cmiddle(Node *head) {
    Node *slow, *fast;
    slow = fast = head;

    while (fast->next != head && fast->next->next != head) {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow;
}

Node* cend(Node *head) {
    if (!head) return NULL;
    Node *ptr = head;
    while (ptr->next != head) ptr = ptr->next;
    return ptr;
}

std::string visualize(Node *head) {
    if (head == NULL) return "";
    if (head->next == head) return std::to_string(head->data);

    std::string visualized_list = "";
    Node *ptr = head;
    while (ptr->next != head) {
        visualized_list += std::to_string(ptr->data) + " -> ";
        ptr = ptr->next;
    }

    return visualized_list + std::to_string(ptr->data) + " -> HEAD";
}

void split_list(Node *head, Node **first, Node **second) {
    Node *middle = cmiddle(head);
    Node *end = cend(head);

    *second = middle->next;
    end->next = *second;

    *first = head;
    middle->next = head;
}

int main() {
    std::vector<int> arr = {1, 2, 6, 3, 4, 8, 9};
    Node *clist = array_to_clist(arr);

    std::cout << visualize(clist) << std::endl;

    Node *first, *second;
    split_list(clist, &first, &second);
    std::cout << visualize(first) << std::endl;
    std::cout << visualize(second) << std::endl;

    return 0;
}