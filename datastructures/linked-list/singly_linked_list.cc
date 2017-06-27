#include <iostream>
#include <string>
#include <stdexcept>

// Node Structure
struct node {
    int data;
    node *next;

    // Default constructor - resets data to 0.
    node() {
        data = 0;
        next = NULL;
    }

    // Set data constructor
    node(int data) {
        this->data = data;
        next = NULL;
    }

    // Set data and next constructor
    node(int data, node *next) {
        this->data = data;
        this->next = next;
    }
};

class linked_list {
    node *head; // Head pointer

public:
    // Default constructor
    linked_list() {
        head = new node();
    }

    // Set head value constructor
    linked_list(int data) {
        head = new node(data);
    }

    // Set head node constructor
    linked_list(node *head) {
        this->head = head;
    }

    // check if the list is empty
    bool is_empty() {
        return !head;
    }

    // push value
    node* push(int data) {
        node *temp = new node(data);
        temp->next = head;
        return head = temp;
    }

    // push node
    node* push(node *new_node) {
        new_node->next = head;
        return head = new_node;
    }

    // pop node
    int pop() {
        if (this->is_empty()) {
            throw "Empty List Exception";
        }
        node *temp = head;
        int val = temp->data;
        head = head->next;
        delete temp;
        return val;
    }

    // peek head node value
    int peek() {
        if (this->is_empty()) {
            throw "Empty List Exception";
        }
        return head->data;
    }

    // insert data at particular position
    node* insert(int data, int position) {
        return this->insert(new node(data), position);
    }

    // insert node at particular position
    node* insert(node *new_node, int position) {
        if (this->is_empty()) {
            return head = new_node;
        }

        node *current = head;
        position--;
        while (position && current->next) {
            current = current->next;
            position--;
        }
       new_node->next = current->next;
       current->next = new_node;

       return head;
    }

    // remove first occurence of data
    void remove(int data) {
        if (this->is_empty()) {
            throw "Empty List Exception";
        }

        if (head->data == data) {
            this->pop();
        }

        node *current = head;
        while (current->next && current->next->data != data) {
            current = current->next;
        }

        if (current->next) {
            node *temp = current->next;
            current->next = temp->next;
            delete temp;
        }
    }

    // Visualize the list
    std::string show() {
        node *current = head;
        std::string visualized_list = "";
        if (this->is_empty()) {
            return "";
        }

        if (current && !current->next) {
            return std::to_string(current->data);
        }

        while (current->next) {
            visualized_list += std::to_string(current->data) + " -> ";
            current = current->next;
        }
        return visualized_list.substr(0, visualized_list.length() - 4);
    }

    // destructor
    ~linked_list() {
        node *current;
        while (head) {
            current = head;
            head = head->next;
            delete current;
        }
    }
};

int main(int argc, char *argv[]) {
    linked_list my_list;
    my_list.push(3);
    my_list.push(4);
    my_list.push(5);
    my_list.push(6);
    my_list.push(7);
    my_list.push(8);
    my_list.push(9);
    my_list.push(10);
    my_list.push(11);
    std::cout << my_list.show() << "\n";

    my_list.pop();
    my_list.pop();
    my_list.pop();
    my_list.pop();
    std::cout << my_list.show() << "\n";

    my_list.insert(15, 3);
    my_list.remove(6);
    my_list.remove(8);
    std::cout << my_list.show() << "\n";
}
