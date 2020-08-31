class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def delete_middle_node(node):
    # Assumes node.next exists
    node.data = node.next.data
    node.next = node.next.next


def compare_lists(l1, l2):
    while l1 != None and l2 != None and l1.data == l2.data:
        l1 = l1.next
        l2 = l2.next

    return l1 == None and l2 == None


if __name__ == '__main__':
    ll_1 = LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(3, LinkedList(4)))))
    output_1 = LinkedList(1, LinkedList(1, LinkedList(3, LinkedList(4))))

    delete_middle_node(ll_1.next)
    assert compare_lists(ll_1, output_1)
