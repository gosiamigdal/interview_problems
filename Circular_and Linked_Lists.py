# Circular lists 

class ListElement():
    def __init__(self, element, next):
        self.element = element
        self.next = next

class List():
    def __init__(self):
        self.head = ListElement(None, None)
        self.head.next = self.head
    def prepend(self, new_element):
        list_element = ListElement(new_element, self.head.next)
        self.head.next = list_element
    def items(self):
        current = self.head.next
        while current != self.head:
            yield current.element
            current = current.next
    def size(self):
        suma = 0
        current = self.head.next
        while current != self.head:
            suma += 1
            current = current.next
        return suma 
    def search(self, item):
        current = self.head.next
        while current != self.head:
            if current.element == item:
                return current
            else:
                current = current.next
        return None
    def remove(self, item):
        previous = self.head
        current = self.head.next
        while current != self.head:
            if current.element == item:
                previous.next = current.next
                return True 
            else:
                current = current.next
                previous = previous.next
        return False 
    def append(self, item):
        current = self.head.next
        while current.next != self.head:
            current = current.next
        list_element = ListElement(item, self.head)
        current.next = list_element
    def insert(self, item, index):
        if self.size() <= index:
            return False 
        current = self.head.next
        current_index = 0
        while index != current_index:
            current_index += 1
            current = current.next
        list_element = ListElement(item, current.next)
        current.next = list_element
        return True
    def remove_at_given(self, index):
        if self.size() <= index:
            return False
        previous = self.head
        current = self.head.next
        current_index = 0
        while current_index != index:
            current_index += 1
            current = current.next
            previous = previous.next
        previous.next = current.next
        return True 
    def pop(self):
        current = self.head.next
        previous = self.head
        while current.next != self.head:
            current = current.next
            previous = previous.next
        previous.next = self.head
        return current.element 





test = List()
test.prepend(1)
test.prepend(12)
test.prepend(16)
test.prepend(129)
print "Test prepend", [i for i in test.items()] == [129, 16, 12, 1]
print "Test size", test.size() == 4 
print "Test find element", test.search(12).element == 12
print "Not in a list", test.search(88) == None
print "Remove item", test.remove(129) == True and [i for i in test.items()] == [16, 12, 1]
print "Remove non existing", test.remove(222) == False 
test.append("Gosia")
print "Append works", [i for i in test.items()] == [16, 12, 1, "Gosia"]
print "Insert works", test.insert(444, 1) == True and [i for i in test.items()] == [16, 12, 444, 1, "Gosia"]
test.remove_at_given(0)
print "Removing works", [i for i in test.items()] == [12, 444, 1, "Gosia"]


# Linked Lists - typical ones

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None 

    def prepend(self, item):
        new_node = Node(item, self.head)
        self.head = new_node


    def append(self, item):
        new_node = Node(item, None)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node


    def size(self):
        size = 0
        current = self.head
        while current != None:
            size += 1
            current = current.next
        return size 

    def search(self, item):
        current = self.head
        found = False
        while current != None and found != True:
            if current.data != item:
                current = current.next
            else:
                found = True 
        return current 

    def remove(self, item):
        if self.is_empty() == True:
            return False
        if self.head.data == item:
            self.head = self.head.next
            return True
        previous = self.head
        current = self.head.next
        while current.data != item:
            previous = previous.next
            current = current.next
            if current == None:
                return False
        previous.next = current.next
        return True 

    def printer(self):
        if self.is_empty() == True:
            return None 
        current = self.head
        while current != None:
            print current.data
            current = current.next

    def insert(self, item, index):
        if self.size() <= index:
            return False 
        current = self.head
        current_index = 0
        while current_index != index:
            current_index += 1
            current = current.next
        list_element = ListElement(item, current.next)
        current.next = list_element
        return True


    def pop(self):
        if self.is_empty() == True:
            return None
        if self.head.next == None:
            self.head = None
            return self.head.next
        previous = self.head
        current = self.head.next
        while current.next != None:
            current = current.next
        previous.next = None
        return current 

    def remove_at_index(self, index):
        if self.size() <= index:
            return False
        previous = self.head
        current = self.head.next
        current_index = 0
        while current_index != index:
            current_index += 1
            previous = previous.next
            current.current.next
        previous.next = current.next





new_list = LinkedList()
new_list.prepend(12)
new_list.prepend(122)
new_list.prepend(132)
new_list.prepend(1233)
new_list.printer()
















