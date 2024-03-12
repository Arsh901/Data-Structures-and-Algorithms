# Creating the Node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None     # Initially we set next to Null as we don't know the next node address

# Creating the Linked list class

class LinkedList:

    # Initializing an empty linked list
    def __init__(self):
        self.head = None    # Head and tail are pointers pointing to nodes, Head will point to first node while tail to last.
        self.tail = None
        self.length = 0

    # Print the linked list. For this we use the __str__ function of Python
    def __str__(self):
        if self.length == 0:
            return "Empty Linked list"
        else:
            temp_node = self.head
            result = ""
            for i in range(self.length):
                result += str(temp_node.value)
                if temp_node.next is not None:
                    result += "-->"
                temp_node = temp_node.next
        return result

    # Adding nodes to an empty linked list (Adding at the end of the link list)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Inserting a node at the beginning of a Linked list
    def add_node_beg(self, value):
        new_first_node = Node(value)  # Creating the node to be added at beginning
        if self.head is None:
            self.head = new_first_node
            self.tail = new_first_node
        else:
            new_first_node.next = self.head      # At this point self.head points to the current first node. So if we do new_first_node.next = self.head, new_first_node will point to current first node
            self.head = new_first_node
        self.length += 1

    # Inserting element at a given index
    def insert_at_index(self, value, index): # Negative index is not allowed
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        else:
            if self.head is not None:
                if index != 0:  # If index is 0 that means we are adding at the beginning so we can directly use the previously defined function.
                    temp_node = self.head
                    for i in range(index-1):
                        temp_node = temp_node.next
                    new_node.next = temp_node.next
                    temp_node.next = new_node
                    self.length += 1    #This statement is important as without this the entire linked list won't be printed
                else:
                    new_list.add_node_beg(value)
            else:
                self.head = new_node
                self.head = new_node

    # Traversal in a Linked list to access elements
    def traverse(self):      #Note that traverse will print all the values of the linked list
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next  # Moving the temp_node to the next node

    # Searching for an element in the linked list
    def search(self, target_value):
        temp_node = self.head
        for i in range(self.length):
            if temp_node.value == target_value:
                print(f"Target value {target_value} found at index: {i}")
            else:
                if temp_node.next is None:
                    print("Value not found inside the list")
                else:
                    temp_node = temp_node.next

    # Get method of linked list -- We pass index as input to fetch the element
    def get(self, index):
        temp_node = self.head
        if index>self.length:
            print(f"Index entered beyond the length of Linked list")
        elif index<0:
            print("Negative index")
        else:
            for i in range(index):
                temp_node = temp_node.next
            print(f"Element found at index {index}: {temp_node.value}")

    # Set method -- Used to update the value of a node based on index
    def set_value(self, index, new_value):
        temp_node = self.head
        if index>self.length:
            print(f"Index entered beyond the length of Linked list")
        elif index<0:
            print("Negative index")
        else:
            for i in range(index):
                temp_node = temp_node.next
            temp_node.value = new_value

    # Pop FIRST method - Removes the first node from the list and returns that node. Time and space complexity is O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next
            temp_node.next = None
        self.length -= 1
        return temp_node

    # Pop method - Removes the last node from the linked list and returns it
    # Time complexity is O(n), space complexity is O(1)
    def pop(self):
        if self.length == 0:
            return None
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node = self.tail.next
            self.tail.next = None
        self.length -= 1
        return temp_node

    # Remove method - removes a node at a given index
    # Time Complexity = O(n) and space C = O(1)
    def remove(self, index):
        if self.length == 0 or index<0 or index>self.length:
            return None
        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
        else:
            if index == 0:
                return self.pop_first()
            elif index == self.length-1:
                return self.pop()
            else:
                temp_node1 = self.head  #Will be sent to node to be removed
                temp_node2 = self.head  #Will be sent to nod prior to the node to be removed
                for i in range(index):
                    temp_node1 = temp_node1.next
                for i in range(index-1):
                    temp_node2 = temp_node2.next
                temp_node2.next = temp_node1.next
                temp_node1.next = None
                self.length -= 1

    # Delete entire linked list
    def delete_all(self):
        if self.length == 0:
            print("No linked list initialized")
        else:
            self.head = None
            self.tail = None
            self.length = 0

    # Reverse a Linkedlist
    def reverse(self):
        l = []
        temp_node = self.head
        for i in range(self.length):
            l.append(temp_node.value)
            temp_node = temp_node.next
        res = ""
        for i in range(len(l) - 1, -1, -1):
            res = res + str(l[i])
            if i != 0:
                res += " -> "
        print(res)

    # Finding the middle of a linked list
    def find_middle(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp_node = self.head
            return temp_node.value
        else:
            temp_node = self.head
            j = int(self.length / 2)
            for i in range(j):
                temp_node = temp_node.next
            return temp_node.value

    # Removing duplicates in a Linked List
    def remove_duplicates(self):
        if self.length == 0:
            return None
        l = []
        temp_node = self.head
        for i in range(self.length):
            if temp_node.value not in l:
                l.append(temp_node.value)
            temp_node = temp_node.next
        res = ""
        for i in range(len(l)):
            res += str(l[i])
            if i != len(l) - 1:
                res += " -> "
        return res




new_list = LinkedList()
new_list.append(10)
new_list.append(20)
new_list.append(30)
print(f"Result for making a linked list: {new_list}")
new_list.add_node_beg(40)
print(f"Result for adding a node valued 40 at beginning: {new_list}")
new_list.insert_at_index(50,2)
print(f"Result for insertion of 50 at the index 2: {new_list}")
new_list.traverse()
new_list.search(20)
print(new_list.get(2))
new_list.set_value(3, 200)
print(f"New linked list after updating the value of a node: {new_list}")
# print(new_list.pop_first())
# print(f"Linked List after pop_first method: {new_list}")
# new_list.pop()
# print(f"Linked list after pop method that removes last element: {new_list}")
new_list.remove(2)
print(new_list)













