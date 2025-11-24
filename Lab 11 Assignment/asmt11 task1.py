class Stack:
    """
    A simple Stack implementation using Python list.
    Supports push, pop, peek, and is_empty operations.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop and return the top item of the stack."""
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty. Nothing to peek."
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


# -------- MENU DRIVEN USER INPUT --------

stack = Stack()

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        item = input("Enter item to push: ")
        stack.push(item)
        print("Pushed:", item)

    elif choice == "2":
        print("Popped:", stack.pop())

    elif choice == "3":
        print("Top Element:", stack.peek())

    elif choice == "4":
        print("Is Stack Empty?:", stack.is_empty())

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter between 1–5.")