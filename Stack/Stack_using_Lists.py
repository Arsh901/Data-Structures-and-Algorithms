"""
Stack can be implemented using :
1. List - Easy to implement but speed problem when size grows
2. Linked list - fast performance but implementation is hard
"""


# Stack using Python List - No size limit for elements
class Stack:
    def __init__(self):
        self.list = []
        self.length = 0

    def __str__(self):
        """
        When inserting a new element in a list it is always inserted at the last. To implement the stack,
        the last element has to be fetched first. So to do so, we made another list of values that has elements in reversed order.
        """
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # isEmpty Operation: To check if the stack is empty or not
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # Push Method: Insert an element into the stack
    def push(self, value):
        self.list.append(value)
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "No element in the stack"
        else:
            self.list.remove(self.list[len(self.list)-1])
            self.length -= 1

    # Peek: Returns that last element in the stack
    def peek(self):
        if self.isEmpty():
            return "No element in the list"
        else:
            return self.list[len(self.list)-1]

    def delete_all(self):
        self.list = None
        self.length = 0



s = Stack()
s.push(0)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.length)
print(s)
s.pop()
s.pop()
print(s)
print(s.length)
print(s.peek())






