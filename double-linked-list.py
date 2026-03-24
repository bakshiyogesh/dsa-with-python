class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
     
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if not self.head:
            self.head = new_node
            return
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_at_middle(self,data,value):
        new_node=Node(data)
        current=self.head
        if not self.head:
            self.head = new_node
            return
        while current:
            if current.data == value:
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                new_node.next.prev = new_node
                return
            current = current.next
    def delete(self, value):
        current = self.head
        if not current:
            return
        if current.data == value:
            self.head = current.next
            return
        while current:
            if current.data == value:
                if not current.next:
                    current.prev.next = None
                    return
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return
            current = current.next
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


double_list = DoubleLinkedList()
double_list.insert_at_beginning(1)
double_list.insert_at_beginning(2)
double_list.insert_at_beginning(3)
double_list.insert_at_middle(4, 2)
double_list.print_list()
double_list.delete(2)
double_list.print_list()
