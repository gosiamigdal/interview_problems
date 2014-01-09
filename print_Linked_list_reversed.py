# Print the elements of a linked list in reverse

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self):
        self.head = None

    def print_list_in_reverse(self):
        d = {}
        current = self.head
        current_index = 0
        list_of_indexes = []
        while current != None:
            d[current_index] = current
            list_of_indexes.append(current_index)
            current = current.next
            current_index += 1
        for i in list_of_indexes:
            print d[len(list_of_indexes) - i - 1]
