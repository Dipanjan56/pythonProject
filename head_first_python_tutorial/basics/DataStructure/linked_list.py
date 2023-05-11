class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        if position <= 0:
            self.prepend(data)
        if position >= self.length():
            self.append(data)
        else:
            new_node = ListNode(data)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


if __name__ == '__main__':
    my_list = LinkedList()

    # Append elements to the list
    my_list.append(5)
    my_list.append(10)
    my_list.append(20)

    # Display the list
    my_list.printList()  # Output: 5 -> 10 -> 20

    # Prepend an element to the list
    my_list.prepend(0)

    # Display the list
    my_list.printList()  # Output: 0 -> 5 -> 10 -> 20

    # insert data in list
    my_list.insert(15, 3)

    # Display the list
    my_list.printList()  # Output: 0 -> 5 -> 10 -> 15 -> 20

    # Delete an element from the list
    my_list.delete(10)

    # Display the list
    my_list.printList()  # Output: 0 -> 5 -> 15 -> 20

    # Search for an element in the list
    print(my_list.search(5))  # Output: True
    print(my_list.search(20))  # Output: False
