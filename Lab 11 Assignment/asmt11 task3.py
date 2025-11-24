class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ---------- USER INPUT ----------
ll = LinkedList()

# Insert at beginning
item1 = input("Enter an item to insert at beginning: ")
ll.insert_at_beginning(item1)

# Insert two items at end
item2 = input("Enter first item to insert at end: ")
item3 = input("Enter second item to insert at end: ")

ll.insert_at_end(item2)
ll.insert_at_end(item3)

print("\nLinked List:")
ll.display()