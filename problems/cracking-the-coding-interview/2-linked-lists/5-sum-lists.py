class LinkedList:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __str__(self):
        ptr = self
        string = str(ptr.data)
        ptr = ptr.next

        while ptr:
            string += '-> ' + str(ptr.data)
            ptr = ptr.next

        return string

    def compare(self, l2):
        l1 = self
        while l1 != None and l2 != None and l1.data == l2.data:
            l1 = l1.next
            l2 = l2.next

        return l1 == None and l2 == None


def sum_lists_reversed(l1, l2):
    new_list = dummy = LinkedList(-1)

    carry = 0
    while l1 and l2:
        currentSum = l1.data + l2.data + carry
        carry = currentSum // 10
        currentSum %= 10

        dummy.next = LinkedList(currentSum)
        dummy = dummy.next

        l1 = l1.next
        l2 = l2.next

    remaining = l1 if l2 is None else l2

    while remaining:
        currentSum = remaining.data + carry
        carry = currentSum // 10
        currentSum %= 10

        dummy.next = LinkedList(currentSum)

        dummy = dummy.next
        remaining = remaining.next

    if carry:
        dummy.next = LinkedList(carry)

    return new_list.next


def sum_lists(l1, l2):
    l1Num, l2Num = 0, 0

    while l1:
        l1Num *= 10
        l1Num += l1.data

        l1 = l1.next

    while l2:
        l2Num *= 10
        l2Num += l2.data

        l2 = l2.next

    total = str(l1Num + l2Num)
    head = ptr = LinkedList(-1)
    for char in total:
        ptr.next = LinkedList(int(char))
        ptr = ptr.next

    return head.next

if __name__ == '__main__':
    l1 = LinkedList(7, LinkedList(1, LinkedList(6)))
    l2 = LinkedList(5, LinkedList(9, LinkedList(2)))

    output_12 = LinkedList(2, LinkedList(1, LinkedList(9)))

    l3 = LinkedList(9, LinkedList(9))
    l4 = LinkedList(1)

    output_34 = LinkedList(0, LinkedList(0, LinkedList(1)))

    assert sum_lists_reversed(l1, l2).compare(output_12)
    assert sum_lists_reversed(l3, l4).compare(output_34)

    output_342 = LinkedList(1, LinkedList(0, LinkedList(0)))

    assert sum_lists(l3, l4).compare(output_342)
