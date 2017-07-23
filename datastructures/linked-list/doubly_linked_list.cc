#include <iostream>
#include <string>

struct node {
    int data;
    node *next, *previous;

    // Default constructor - resets data to 0.
    node() {
        data = 0;
        next = NULL;
        previous = NULL;
    }

    // Set data constructor
    node(int data) {
        this->data = data;
        next = NULL;
        previous = NULL;
    }

    // Set data and next constructor
    node(int data, node *next, node *previous) {
        this->data = data;
        this->next = next;
        this->previous = previous;
    }
};

class doubly_linked_list {
    node *head;

public:
   // default constructor
   doubly_linked_list() {
        head = new node();
   }

   // set head value constructor
   doubly_linked_list(int data) {
       head = new node(data);
   }

   // set head node constructor
   doubly_linked_list(node *head) {
       this->head = head;
   }

   // check if the list is empty
   bool is_empty() {
       return !head;
   }

   // push value
   node* push(int data) {
       node *temp = new node(data);
       return this->push(temp);
   }

   // push node
   node* push(node *new_node) {
       head->previous = new_node;
       new_node->next = head;
       return head = new_node;
   }

   // pop node
   int pop() {
       if (this->is_empty()) {
           throw "The List is Empty";
       }

       node *temp = head;
       head = head->next;
       head->previous = NULL;
       int val = temp->data;
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
    ~doubly_linked_list() {
        node *current;
        while (head) {
            current = head;
            head = head->next;
            delete current;
        }
    }
};

int main() {
    doubly_linked_list my_list;
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
}
