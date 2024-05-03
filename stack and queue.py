# stack by using list
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from the empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("pop from the empty stack")

    def size(self):
        return len(self.items)

stack_instance = Stack()
print('is the stack empty', stack_instance.is_empty())
stack_instance.push(1)
stack_instance.push(5)
stack_instance.push(3)
print('stack', stack_instance.items)
print('top of the stack', stack_instance.peek())
print('pop', stack_instance.pop())

# queue with list
class QueueList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('dequeue from an empty queue ')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('peek from an empty queue')

    def size(self):
        return len(self.items)

queue_instance = QueueList()
queue_instance.enqueue(1)
queue_instance.enqueue(2)
queue_instance.enqueue(3)
print('front of the queue:', queue_instance.peek())
print("dequeue", queue_instance.dequeue())
print('size of the queue:', queue_instance.size())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

stack_instance = Stack()
stack_instance.push(1)
stack_instance.push(2)
stack_instance.push(3)
stack_instance.display()
print("Popped:", stack_instance.pop())
print("Peek:", stack_instance.peek())
stack_instance.display()

# queue with linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeue_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeue_item
        else:
            raise IndexError('dequeue from an empty queue:')

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError('peek from an empty queue')

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

queue_instance = QueueLinkedList()
queue_instance.enqueue(1)
queue_instance.enqueue(2)
queue_instance.enqueue(3)
print("front of the queue:", queue_instance.peek())
print("Dequeue:", queue_instance.dequeue())
print("Size of the queue", queue_instance.size())
