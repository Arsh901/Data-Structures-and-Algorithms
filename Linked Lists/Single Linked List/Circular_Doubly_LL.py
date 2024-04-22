# In this Linked list, the last node points to the first node and vice versa.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = self.head
            self.head.prev = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp is self.head:
                break
            else:
                result += "<->"
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
        self.length += 1

    def traversal(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.head:
                    break

    def reverse_traversal(self):
        if self.head is None:
            return None
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev
                if temp == self.tail:
                    break

    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return f"Target value found at index {index}."
            else:
                temp = temp.next
                index += 1
            if temp is self.head:
                break
        return "Target value not found."

    def get(self, index):
        if index > self.length-1 or index < 0:
            return None
        if index > self.length//2:
            temp = self.tail
            for i in range(self.length-index-1):
                temp = temp.prev
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
        return temp.value

    def set(self, index, value):
        if index < 0 or index > self.length - 1:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            self.prepend(value)
        new_node = Node(value)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        new_node.next.prev = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            temp.next = None
            self.tail = temp.prev
            temp.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return temp


    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp.prev = None
            self.head = temp.next
            temp.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return temp

    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return None
        if self.head is None:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
        self.length -= 1

    def delete_all(self):
        if self.head is None:
            return None
        self.head = None
        self.tail = None
        self.length = 0

l = CDLinkedList()
l.append(100)
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)