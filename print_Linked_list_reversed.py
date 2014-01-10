# Print the elements of a linked list in reverse

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def print_list_in_reverse2(self):
        if self.next != None:
            self.next.print_list_in_reverse2()
        print self.data



class Linked_list():
    def __init__(self):
        self.head = None

    def print_list_in_reverse(self):
        l = []
        current = self.head
        while current != None:
            l.append(current)
            current = current.next
        for i in range(len(l)):
            print l[len(l) - 1 - i]


