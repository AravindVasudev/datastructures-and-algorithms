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

Node* reverse(Node *head, int k) {
    Node *current = head, *prev = NULL, *next = NULL;
    int count = 0;
    while (current != NULL && count++ < k) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    if (next != NULL) head->next = reverse(next, k);
    return prev;
}

int main() {
    std::vector<int> arr1 = {2, 5, 6, 1, 9, 10, 45};
    std::vector<int> arr2 = {4 , 7, 8, 10, 15, 22, 1};
    std::vector<int> arr3 = {1, 92, 1, 4};

    Node *list1 = array_to_list(arr1);
    Node *list2 = array_to_list(arr2);
    Node *list3 = array_to_list(arr3);

    std::cout << visualize(list1) << "\n" << visualize(reverse(list1, 3)) << "\n\n";
    std::cout << visualize(list2) << "\n" << visualize(reverse(list2, 2)) << "\n\n";
    std::cout << visualize(list3) << "\n" << visualize(reverse(list3, 6)) << "\n\n";

    return 0;
}