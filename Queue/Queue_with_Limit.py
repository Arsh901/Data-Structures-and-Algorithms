# Queue with limited size (Circular queue). Two pointers - front and rear are used

""" In a circular queue, once you remove an element from a completely filled queue
and then add one, rear goes to 0 where that new element is stored. Remove another element,
and add another, it is incremented by one. """

class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = [None]*self.maxsize
        self.front = -1
        self.rear = -1

    def __str__(self):
       l = [str(i) for i in self.list]
       return " ".join(l)

    def isFull(self):
        if self.rear + 1 == self.front:
            return True
        elif self.rear + 1 == self.maxsize and self.front == 0:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
            return
        else:
            if self.front == -1 and self.rear == -1:
                self.front = 0
                self.rear = 0
            else:
                if self.front == 0 and self.rear < self.maxsize - 1:
                    self.rear += 1
                elif self.front > 0 and self.rear == self.maxsize-1:
                    self.rear = 0
                elif self.front > 0 and self.rear >= 0:
                    self.rear += 1
            self.list[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            start = self.front
            if self.front == 0 and self.rear == 0:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxsize:
                self.front = 0
            else:
                self.front += 1
            self.list[start] = None

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            return self.list[self.front]

    def delete(self):
        self.list = self.maxsize = None
        self.front = -1
        self.rear = -1
        



q = Queue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q)
q.enqueue(50)
q.dequeue()
q.dequeue()
q.dequeue()

print(q.peek())







