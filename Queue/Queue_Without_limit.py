""" A linear data structure that follows FIFO functionality. """

""" Applications - A printer queue or a call center phone system where many customer
 call at the call center but are aligned in a queue till their turn comes. """

# Queue can be implemented using Python lists or Linked lists.
# Using lists, its possible to either have a capacity or infinite space.

class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        l = [str(x) for x in self.list]
        return " ".join(l)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Not element to remove")
            return
        self.list.remove(self.list[0])

    def peek(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        else:
            return self.list[0]

    def delete(self):
        self.list = []
        

q = Queue()
print(q.isEmpty())
q.dequeue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)
q.dequeue()
print(q)







