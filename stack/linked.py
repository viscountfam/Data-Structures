class Linked_list:
    """
    Data:
    1. A reference to the first node (Head) in the list
    2. A reference to the end node (Tail) in the list

    Behavior:
    1. Append (Add a new node to the Node 
    referenced by the Tail and make that new Node the tail)
    2. Prepent (Add a new node and point that Node's next_node at the old Head; update Head Pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum

    """
    def __init__(self):
        self.head = None
        self.tail = None
        # There is more than one way to write a linked list class 
        # what is important is that your linked list can do all the things that you need it to
        # A linked only stores pointers to heads and tails and isn't even truly a container for nodes
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_head(self):
        if self.head is None:
            return None
        # LL of one item
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()
        # More than one item
        value = self.head.get_value
        self.head = self.head.get_next()
        return value
    def remove_tail(self):
        if self.tail is None:
            return None
        else:
            return None
    def get_maximum(self):
        highest_value = 0
        currentval = self.head
        nextval = self.head.next_node
        while next != None:
            if currentval > highest_value:
                highest_value = currentval
                currentval = nextval
                nextval = nextval.next_node
            else:
                currentval = nextval
                nextval = nextval.next_node
    
        return highest_value




class Node:
    """""
    Data:
    Stores two pieces of data, the value, and the pointer to next_node
    1. The value
    2. The Next Node
    Operations:
    1. Get value from node
    2. add a new node as next
    3. Set the value of the node
    4. Get the value of the next node
    """""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next
        return self.next_node

    def set_value(self, new_value):
        self.value = new_value
        return f"value is now {new_value}"
