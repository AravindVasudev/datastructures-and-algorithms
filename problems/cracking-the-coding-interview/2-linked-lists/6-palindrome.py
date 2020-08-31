class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __str__(self):
        ptr = self
        string = str(ptr.data)
        ptr = ptr.next

        while ptr:
            string += ' -> ' + str(ptr.data)
            ptr = ptr.next

        return string

    def compare(self, l2):
        l1 = self
        while l1 != None and l2 != None and l1.data == l2.data:
            l1 = l1.next
            l2 = l2.next

        return l1 == None and l2 == None

    @staticmethod
    def from_iterable(data):
        head = dummy = Node(-1)
        for el in data:
            dummy.next = Node(el)
            dummy = dummy.next

        return head.next


def is_palindrome(linked_list):
    slow, fast = linked_list, linked_list
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow and stack:
        if slow.data != stack[-1]:
            return False

        slow = slow.next
        stack.pop()

    return not slow and not stack

if __name__ == '__main__':
    ll_1 = Node.from_iterable('tacocat')
    ll_2 = Node.from_iterable('madam')
    ll_3 = Node.from_iterable('abba')
    ll_4 = Node.from_iterable('abbc')

    assert is_palindrome(ll_1)
    assert is_palindrome(ll_2)
    assert is_palindrome(ll_3)
    assert not is_palindrome(ll_4)
