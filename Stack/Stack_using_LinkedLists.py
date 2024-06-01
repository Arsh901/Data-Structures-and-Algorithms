"""Implementation of Stack using Linked Lists. Nodes are created and inserted in the stack as elements. The
 node at the top of the stack represents the first element of the linked list or the top of stack """

""" Stack is useful while implementing LIFO functionality. In cases like reversing a string, etc.
Problem is we cannot access an element randomly. We need to remove each element before reaching the 
target. Case of data corruption is minimal. """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        # Create a linked list object here in this stack function
        self.LinkedList = LinkedList()
        self.length = 0

    def __str__(self):
        temp = self.LinkedList.head
        l = []
        while temp:
            l.append(str(temp.value))
            temp = temp.next
        return "\n".join(l)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
        else:
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node
        self.length += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            temp.next = None
            self.length -= 1
            return temp

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.LinkedList.head.value


    def search(self, value):
        temp = self.LinkedList.head
        i = 0
        while temp:
            if temp.value == value:
                return f"Target value found at index {self.length - i - 1}"
            else:
                temp = temp.next
                i += 1
        return "Value not found"

    def delete(self):
        self.LinkedList.head = None


s = Stack()
print(s.isEmpty())
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.peek())

















