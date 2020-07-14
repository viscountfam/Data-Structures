from singly_linked_list import linked_list, Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        self.size += 1
    def pop(self):
        if len(self.storage)== 0:
            return None
        else:
            return self.storage.pop(-1)
    

class list_Stack:
    def __init__(self):
        self.storage = linked_list()
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    def pop(self):
        self.storage.remove_tail()
        self.size += 1
    def __len__(self):
        return self.size