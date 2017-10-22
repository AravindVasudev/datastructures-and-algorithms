#include <iostream>
#include <stack>

struct Node {
    int data;
    Node *next;
};

int intersection(Node *list1, Node *list2) {
    std::stack<Node*> stack1, stack2;
    Node *ptr = NULL;

    while (list1) {
        stack1.push(list1);
        list1 = list1->next;
    }

    while (list2) {
        stack2.push(list2);
        list2 = list2->next;
    }

    while (stack1.top() == stack2.top()) {
        ptr = stack1.top();
        stack1.pop();
        stack2.pop();
    }

    return ptr ? ptr->data : -1;

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

int main() {
    Node *list1, *list2, *ptr;

    list1 = ptr = new Node {1, NULL};
    for (int i = 2; i <= 5; i++) {
        ptr->next = new Node {i, NULL};
        ptr = ptr->next;
    }

    list2 = ptr = new Node {6, NULL};
    for (int i = 7; i <= 8; i++) {
        ptr->next = new Node {i, NULL};
        ptr = ptr->next;
    }

    ptr->next = list1->next->next->next;

    std::cout << "List 1: " << visualize(list1) << std::endl;
    std::cout << "List 2: " << visualize(list2) << std::endl;
    std::cout << "The intersection node is " << intersection(list1, list2) << std::endl;
}