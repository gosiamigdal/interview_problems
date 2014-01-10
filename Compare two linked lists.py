class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def are_similar(self, list2):
        l1 = []
        l2 = []
        current = self.head
        while current != None:
            l1.append(current)
            current = current.next
        current2 = list2.head
        while current2 != None:
            l2.append(current)
            current2 = current2.next
        return l1 == l2

     def are_similar(self, list2):
        current = self.head
        current2 = list2.head
        while current != None and current2 != None:
            if current.data != current2.data:
                return False
            current = current.next
            current2 = current2.next
        return current == current2