class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def get_kth_to_last(linked_list, k):
    if not linked_list or k < 0:
        return None

    slow, fast = linked_list, linked_list

    while fast.next:
        if k <= 0:
            slow = slow.next

        fast = fast.next
        k -= 1

    return slow


if __name__ == '__main__':
    ll_1 = LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(3, LinkedList(4)))))
    k_1 = 1
    output_1 = 3

    k_2 = 2
    output_2 = 1

    k_3 = 4
    output_3 = 1

    k_4 = 0
    output_4 = 4

    assert get_kth_to_last(ll_1, k_1).data == output_1
    assert get_kth_to_last(ll_1, k_2).data == output_2
    assert get_kth_to_last(ll_1, k_3).data == output_3
    assert get_kth_to_last(ll_1, k_4).data == output_4
