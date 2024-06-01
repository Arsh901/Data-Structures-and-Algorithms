# Stack with limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        self.length = 0

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
            self.length += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.list.remove(self.list[len(self.list)-1])
            self.length -= 1

    def peek(self):
        if self.isEmpty():
            return "Stack Empty"
        else:
            return self.list[len(self.list)-1]

    def delete_stack(self):
        self.list = None

    def size(self):
        return f"Size of Stack is {self.length}"

    def search(self, value):
        for i in range(self.length):
            if self.list[i] == value:
                return f"Value found at index {i}"
        return "Value not found"




s = Stack(5)
s.push(0)
s.push(10)
s.push(20)
s.push(30)
print(s)
print(s.isFull())
print(s.isEmpty())
print(s.size())
print(s.search(80))






















