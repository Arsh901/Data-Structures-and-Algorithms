class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.prev}<--{self.value}-->{self.next}"

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):   # O(1) Time Complexity
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "<->"
            temp = temp.next
        return result

    def prepend(self, value):  # O(1) Time complexity
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):     # O(N) Time Complexity
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def reverse_traversal(self):   # O(N) Time Complexity
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev

    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                print(f"Target value found at index {index}")
                temp = temp.next
                index += 1
            else:
                temp = temp.next
                index += 1

    # In Doubly Linked list, we use optimized version of get method. If index > mid, use prev else next.
    def get(self, index):        # O(N) Time Complexity
        if index > self.length - 1 or index < 0:
            return None
        if index < self.length//2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-index-1):
                temp = temp.prev
        return temp.value

    def set(self, index, value):
        if index > self.length - 1 or index < 0:
            return None
        if index < self.length//2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-index-1):
                temp = temp.prev
        temp.value = value

    def insert(self, index, value):
        if index > self.length or index < 0:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            temp1 = self.head
            for i in range(index-1):
                temp = temp.next
                temp1 = temp1.next
            temp1 = temp1.next
            new_node.next = temp.next
            temp.next = new_node
            temp1.prev = new_node
            new_node.prev = temp

    # Pop_First method - Removes the first element from the list.
    def pop_first(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
            self.length -= 1
            return temp

    # Pop method - Removes the last node and return it.
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def remove(self, index):
        if self.head is None:
            return None
        if index > self.length - 1 or index < 0:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            temp = self.head
            temp1 = self.head
            temp2 = self.head
            for i in range(index-1):
                temp = temp.next
                temp1 = temp1.next
            for i in range(index+1):
                temp2 = temp2.next
            temp1 = temp1.next
            temp.next = temp1.next
            temp2.prev = temp
            temp1.next = temp1.prev = None
        self.length -= 1



l = DLList()
l.append(0)
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
print(l)
l.insert(1, 60)
l.remove(3)
l.remove(2)
print(l)



