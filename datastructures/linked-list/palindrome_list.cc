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

Node* reverse_list(Node *head) {
    Node *prev = NULL, *next;
    while (head) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }

    return prev;
}

Node* middle_node(Node *head) {
    Node *fast = head;
    while (fast && fast->next) {
        fast = fast->next->next;
        head = head->next;
    }

    return head;
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

bool is_palindrome(Node* head) {
    Node *p1, *p2;
    p1 = head;
    p2 = reverse_list(middle_node(head)->next);

    bool ans = true;
    while (ans && p2) {
        if (p1->data != p2->data) ans = false;
        p1 = p1->next;
        p2 = p2->next;
    }

    return ans;
}

int main() {
    std::vector<int> arr1 = {1, 2, 1, 3, 4};
    std::vector<int> arr2 = {1, 2, 3, 2, 1};
    std::vector<int> arr3 = {1, 2, 2, 1};

    Node *list1 = array_to_list(arr1);
    Node *list2 = array_to_list(arr2);
    Node *list3 = array_to_list(arr3);

    std::cout << visualize(list1) << " => " << is_palindrome(list1) << std::endl;
    std::cout << visualize(list2) << " => " << is_palindrome(list2) << std::endl;
    std::cout << visualize(list3) << " => " << is_palindrome(list3) << std::endl;
}