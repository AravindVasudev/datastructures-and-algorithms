/**
 * Given a Linked List with even and odd numbers, create an algorithm for making
 * changes to list in such a way that all even numbers appear at the beginning
 **/

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

Node* even_odd_reorder(Node *head) {

}

int main() {
    std::vector<int> arr = {1, 2, 2, 3, 7, 6, 0, 1, 1, 5, 6, 4};
    Node *list = array_to_list(arr);

    std::cout << visualize(list) << "\n" << visualize(even_odd_reorder(list)) << "\n";
}