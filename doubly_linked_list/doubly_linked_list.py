"""
Each ListNode holds a reference to its previous node
as well as tis next node in the list.

"""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


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
        # store the value of the head
        old_head = self.head
        #check to see if the DLL is empty
        # delete the head
        if self.head.next is not None:
            self.head.next.prev = None
        # set head to head.next
            self.head = self.head.next
        # this will delete it's last reference 
        # which will trigger garbage cleanup
        # decrement length
            self.length -= 1
        # return the value of the head
            return old_head
        else:
            self.head = None
            self.tail = None
            self.length = 0
            return None

    def remove_from_tail(self):
        #store the value of the tail
        old_tail = self.tail
        # check to see if the DLL is empty
        if self.tail.prev is not None:
            self.tail.prev.next = None
        # set tail to tail prev
            self.tail = self.tail.prev
        # decrement length
            self.length -= 1
        # return the value of the old tail
            return add_to_tail
        else:
            self.head = None
            self.tail = None
            self.length = 0
            return None

    """
    Removes the input node from its current spot in the List and inserts is as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return None
        else:
            # adjust the pointers of the elements touching the node
            # set the next of the prev node to the node next
            node.prev.next = node.next
            node.next.prev = node.prev
            # adjust the head (this logic should be similar to the logic for add to head)
            node.next = self.head
            # set head's prev to new node
            self.head.prev = node
            # set head to the new node
            self.head = node


    """
    Remove the input node from its current spot in the List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return None
        else:
            # adjust the pointers of the elements touching the node
            # set the next of the prev node to the node next
            node.prev.next = node.next
            node.next.prev = node.prev
            #adjust the tail (this logic should be similar to the logic for add to tail)
            # Assign the newly created node to the current tail's next
            self.tail.next = node
            # Assign the current tail to the newly created node's prev
            node.prev = self.tail
            # Assign self.tail to the newly created node
            self.tail = node

    """
    Deletes the input node from the List, preserving the order of the other elements of the List.
    """
    def delete(self, node):
        # the logic here should be the same as move to end and move to staret without the head and tail adjustments
        if node.prev.next and node.next:
            node.prev.next = node.next
        if node.next.prev and node.prev:
            node.next.prev = node.prev
        return "node was deleted"

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