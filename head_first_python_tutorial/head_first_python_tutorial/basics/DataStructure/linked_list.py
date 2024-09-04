class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert(self, val, position):
        if position <= 0:
            self.prepend(val)
        if position >= self.length():
            self.append(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next

    def search(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
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

    def display(self):
        current = self.head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print("None")


if __name__ == '__main__':
    my_list = LinkedList()

    # Append elements to the list
    my_list.append(5)
    my_list.append(10)
    my_list.append(20)

    # Display the list
    my_list.display()  # Output: 5 -> 10 -> 20

    # Prepend an element to the list
    my_list.prepend(0)

    # Display the list
    my_list.display()  # Output: 0 -> 5 -> 10 -> 20

    # insert val in list
    my_list.insert(15, 3)

    # Display the list
    my_list.display()  # Output: 0 -> 5 -> 10 -> 15 -> 20

    # Delete an element from the list
    my_list.delete(10)

    # Display the list
    my_list.display()  # Output: 0 -> 5 -> 15 -> 20

    # Search for an element in the list
    print(my_list.search(5))  # Output: True
    print(my_list.search(20))  # Output: False
