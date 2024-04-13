class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):   # O(1)
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def __str__(self):
        result = ""
        temp = self.head
        while temp.next is not self.head:
            result += str(temp.value)
            if temp.next == self.head:
                pass
            else:
                result += "-->"
            temp = temp.next
        result += str(self.tail.value)
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def traversal(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.value)
            temp = temp.next
        print(self.tail.value)

    def search(self, value):
        if self.head is None:
            return None
        else:
            temp = self.head
            for i in range(self.length):
                if temp.value != value:
                    temp = temp.next
                    i += 1
                else:
                    return f"Target value found at index {i}."
        return "Target value not found."

    def get(self, index):
        if index < 0 or index > self.length-1:
            return None
        if self.head is None:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return f"Value at index {index} is {temp.value}"

    def set(self, index, value):
        if index < 0 or index > self.length - 1:
            return None
        if self.head is None:
            return None
        temp = self.head
        for  i in range(index):
            temp = temp.next
        temp.value = value

    # Removes a node at a given index and returns it.
    def pop_first(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if self.head is None:
            return None
        if index == 0:
            temp = self.head
            self.tail.next = temp.next
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp
        temp1, temp2 = self.head, self.head
        for i in range(index-1):
            temp2 = temp2.next
        for i in range(index):
            temp1 = temp1.next
        if index == self.length-1:
            self.tail = temp2
            temp2.next = self.head
            temp1.next = None
        else:
            temp2.next = temp1.next
            temp1.next = None
        self.length -= 1
        return temp1

    # Pop Method - Removes the last node and return it
    def pop(self):
        if self.head is None:
            return None
        temp1, temp2 = self.head, self.head
        for i in range(self.length-2):
            temp2 = temp2.next
        for i in range(self.length-1):
            temp1 = temp1.next
        self.tail = temp2
        temp2.next = self.head
        temp1.next = None
        self.length -= 1
        return temp1

    # Remove method-Removes a node at a given value
    def remove(self, value):
        if self.head is None:
            return None
        if value == self.head.value:
            temp = self.head
            self.tail.next = temp.next
            self.head = temp.next
            temp.next = None
            self.length -= 1
        else:
            temp1, temp2 = self.head, self.head
            while temp1.value is not value:
                temp1 = temp1.next
            while temp2.next is not temp1:
                temp2 = temp2.next
            if value == self.tail.value:
                self.tail = temp2
                temp2.next = self.head
                temp1.next = None

            else:
                temp2.next = temp1.next
                temp1.next = None
            self.length -= 1

    # Delete method - Delete the entire linked list
    def delete_all(self):     # O(1) Time complexity
        if self.head is None:
            print("Circular Linked list does not exist")
        else:
            self.tail.next = None
            self.tail = None
            self.head = None
            self.length = 0

    # Count the number of nodes in a circular Linked list
    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next == self.head:
            return 1
        i = 1
        temp = self.head
        while temp.next != self.tail:
            i += 1
            temp = temp.next
        i += 1
        return i



n = CSLinkedList()
n.append(10)
n.append(20)
n.append(30)
n.prepend(0)
n.prepend(70)
n.insert(0, 15)
n.insert(2,100)
print(n.tail.next.value)
print(n.search(30))
print(n.get(7))
n.set(7, 500)
print(n)
n.remove(100)
n.remove(15)
n.remove(30)
print(n.count_nodes())

print(n)

