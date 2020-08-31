class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def partition(linked_list, k):
    ptr = linked_list

    tail = linked_list
    while tail.next:
        tail = tail.next

    while ptr:
        next_node = ptr.next
        ptr.next = None

        if ptr.data < k:
            ptr.next = linked_list
            linked_list = ptr
        else:
            tail.next = ptr
            tail = tail.next

        ptr = next_node


    # tail.next = None
    return linked_list


def compare_lists(l1, l2):
    while l1 != None and l2 != None and l1.data == l2.data:
        l1 = l1.next
        l2 = l2.next

    return l1 == None and l2 == None


if __name__ == '__main__':
    ll = LinkedList(3, LinkedList(5, LinkedList(8, LinkedList(5, LinkedList(10, LinkedList(2, LinkedList(1)))))))
    output = LinkedList(3, LinkedList(1, LinkedList(2, LinkedList(10, LinkedList(5, LinkedList(5, LinkedList(8)))))))

    assert compare_lists(partition(ll, 5), output)
