class Slist:
    def __init__(self) -> None:
        self.head = None
class SLNode:
        def __init__(self) -> None:
            self.value = Value 
            self.next = None

        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            return self
        
        def print_values(self):
            current = self.head
            while current:
                print(current.value)
                current =current.next 

        def add_to_back(self, val):
            if self.head == None:
                self.add_to_front(val)
                return self
            new_node = SLNode(val)
            current = self.head 
            while (current.next !=None):
                current = current.next
                current.next = new_node
                return self        
            
            def remove_from_front(self):
                if self.head != None:
                    self.head = self.head.next
                    return self
                
                def remove_from_back(self):
                    if self.head ==None:
                        return self
                    elif self.head.next ==None:
                        self.head
                        return self
                    else:
                           current = self.head
                    while current.next.next !=None:
                        current = current.next
                        current.next= None
                    return self