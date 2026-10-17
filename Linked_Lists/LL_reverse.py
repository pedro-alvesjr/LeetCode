class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head.next
            pre = self.head
            while (temp.next):
                temp = temp.next
                pre = pre.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, value, index):
        if self.get(index):
            temp = self.get(index)    
            temp.value = value
        else:
            return False
        return True

    def insert(self, value, index):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        elif self.get(index):
            new_node = Node(value)
            if index == 0:
                self.prepend(value)
            else:
                temp, pre = self.get(index), self.get(index - 1)
                pre.next, new_node.next = new_node, temp
        elif index == self.length:
            self.append(value)
        else:
            return False
        self.length += 1
        return True
    
    def remove(self, index):
        if self.length == 0 or index >= self.length or index < 0:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        temp, pre = self.get(index), self.get(index - 1)
        pre.next, temp.next = temp.next, None
        self.length -= 1
        return temp
    
    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()


