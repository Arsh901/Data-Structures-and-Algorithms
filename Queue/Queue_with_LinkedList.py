
"""We use 2 pointers - head and tail, just like in Linked List. Whenever a new element has to
be added, a node will be created and appended at the end of the linked list as it's a queue. In
case of stack the new element was always inserted at the beginning."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
        self.length = 0

    def __str__(self):
        temp = self.LinkedList.head
        l = []
        while temp:
            l.append(str(temp.value))
            temp = temp.next
        return " ".join(l)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            print("Empty queue")
            return
        else:
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            self.length -= 1

    def peek(self):
        if self.isEmpty():
            print("Empty queue")
            return
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print(q.peek())



