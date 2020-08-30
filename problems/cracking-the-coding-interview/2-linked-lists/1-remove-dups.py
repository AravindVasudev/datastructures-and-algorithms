class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def remove_duplicates(linked_list):
    if not linked_list:
        return None

    ptr = linked_list
    seen = set([ptr.data])

    while ptr.next:
        if ptr.next.data in seen:
            ptr.next = ptr.next.next
        else:
            seen.add(ptr.next.data)
            ptr = ptr.next

    return linked_list


def remove_duplicates_followup(linked_list):
    if not linked_list:
        return None

    ptr = linked_list

    while ptr:
        runner = ptr
        while runner.next:
            if ptr.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        ptr = ptr.next

    return linked_list


def compare_lists(l1, l2):
    while l1 != None and l2 != None and l1.data == l2.data:
        l1 = l1.next
        l2 = l2.next

    return l1 == None and l2 == None


if __name__ == '__main__':
    ll_1 = LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(3, LinkedList(4)))))
    ll_1_copy = LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(3, LinkedList(4)))))
    output_1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))

    assert compare_lists(remove_duplicates(ll_1), output_1)
    assert compare_lists(remove_duplicates_followup(ll_1_copy), output_1)

