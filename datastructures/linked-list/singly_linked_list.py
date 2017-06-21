# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List Class
class UnorderedList:
    def __init__(self):
        self.head = None

    # returns true if empty
    def isEmpty(self):
        return self.head == None

    # adds new element to the front of the list
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    # returns dynamically counted size
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count

    # returns node position
    def search(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.data == item:
                return count
            count += 1
            current = current.next
        return -1

    # returns true if the element is in the list
    def exists(self, item):
        return self.search(item) != -1

    # removes first occurence of the item
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if current != None:
            if previous == None:
                self.head = current.next
            else:
                previous.next = current.next

    # visualizes the list for print function
    def __str__(self):
        current = self.head
        visualized = ''
        while current != None:
            visualized += '{} '.format(current.data)
            if current.next != None: visualized += '-> '
            current = current.next

        return visualized


if __name__ == '__main__':
    dummyList = UnorderedList()
    dummyList.add(4)
    dummyList.add(3)
    dummyList.add(2)
    dummyList.add(6)
    dummyList.add(7)

    # Print the list
    print(dummyList)

    # size
    print(dummyList.size())

    # isEmpty
    print(dummyList.isEmpty())

    # search
    print(dummyList.search(2))
    print(dummyList.search(9))

    # exists
    print(dummyList.exists(2))
    print(dummyList.exists(9))

    # remove
    dummyList.remove(2)
    dummyList.remove(9)

    print(dummyList)
