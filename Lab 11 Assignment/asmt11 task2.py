class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# ---- USER INPUT ----
q = Queue()

# Enqueue two items from user
q.enqueue(input("Enter first item: "))
q.enqueue(input("Enter second item: "))

print("Dequeue:", q.dequeue())
print("Is queue empty?", q.is_empty())
print("Dequeue:", q.dequeue())
print("Is queue empty?", q.is_empty())