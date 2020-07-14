"""
Each ListNode holds a reference to its previous node
as well as tis next node in the list.

"""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next: 
            self.next.prev = self.prev


"""
Our doubly-linked list class. 
It holds references to the list's head and tail nodes

"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it as the new head of the list.
    Don't forget to handle the old head node's previous pointer accordingly.

    """

    def add_to_head(self,value):
        # create instance of Listnode with a value
        new_list_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        
        #check if DLL is empty
            # if so set head and tail to the new node instance

        # if DLL is not empty
        if self.head is not None:
                # set new node's next to current head
            new_list_node.next = self.head
                # set head's prev to new node
            self.head.prev = new_list_node
                # set head to the new node
            self.head = new_list_node
        else:
            self.head = new_list_node
            self.tail = new_list_node

    def add_to_tail(self, value):
        # create instance of ListNode with a value
        new_list_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # check to see is DLL is empty
        if self.head is not None:
            # Assign the newly created node to the current tail's next
            self.tail.next = new_list_node
            # Assign the current tail to the newly created node's prev
            new_list_node.prev = self.tail
            # Assign self.tail to the newly created node
            self.tail = new_list_node
        else:
            self.head = new_list_node
            self.tail = new_list_node

    def remove_from_head(self):
        if self.head:
            value = self.head.value
        else:
            value = None
        self.delete(self.head)
        return value

    def remove_from_tail(self):
        if self.tail:
            value = self.tail.value
        else: 
            value = None
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the List and inserts is as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)


    """
    Remove the input node from its current spot in the List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the order of the other elements of the List.
    """
    def delete(self, node):
        # the logic here should be the same as move to end and move to start without the head and tail adjustments
        # if empty
        if not self.head and not self.tail:
            return None
        #if head and tail
        if node == self.head and self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes in the list.

    """
    def get_max(self):
        maximum = 0
        current = self.head
        while current is not None:
            if current.value > maximum:
                maximum = current.value
            current = current.next
        return maximum