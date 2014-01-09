class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def are_similar(self, list2):
        current1 = self.head
        current2 = list2.head
        while current1 != None and current2 != None:
            if current1 != current2:
                return False
            current1 = current1.next
            current2 = current2.next
        return True 
