class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
         
    def insert_at_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def insert_at_middle(self, data,value):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                if current.data == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(current)

    
    def delete(self, data):
        current = self.head
        prev=None
        if not current:
            return
        if current.data == data:
            # prev = None
            self.head = current.next 
            # current = None
            return
        while current.next:
            if current.data == data:
                prev.next = current.next
                # current.next = current.next.next 
                return 
                # break
            prev = current
            current = current.next
        if current.data == data:
            prev.next = None
    

# Example usage:
if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(5)
    ll.print_list()
    ll.delete(2)
    ll.print_list()


# new_node is temp variable
