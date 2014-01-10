# Check, if linked list is a palindrome 

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self):
        self.head = None

    def is_palindrome(self):
        alista = []
        current = self.head
        while current != None:
            reverse.append(current)
            current = current.next
        for i in range(len(alista) / 2):
            if alista[len(alista) - 1 - i] != alista[i]:
                return False
        return True 


        
