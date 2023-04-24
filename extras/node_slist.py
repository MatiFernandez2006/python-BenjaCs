class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	
        return self	
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	
        return self
    def add_to_back(self, val):
        if self.head == None:	
            self.add_to_front(val)	
            return self	
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	
        return self 

    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value
    

    def remove_val(self, val):
        if self.head is None:
            return False
        if self.head.value == val:
            self.head = self.head.next
            return True
        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return True
            runner = runner.next
        return False

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        for _ in range(n - 1):
            if runner is None:
                return None
            runner = runner.next
        if runner is None:
            return None
        new_node.next = runner.next
        runner.next = new_node
        return self



my_list = SList()
my_list.add_to_front(54).add_to_front(26).add_to_front(93).add_to_front(17).add_to_front(77).add_to_front(31)
my_list.print_values() 

removed_value = my_list.remove_from_front()
print(f"Removed value: {removed_value}") 
my_list.print_values() 

removed_value = my_list.remove_from_back()
print(f"Removed value: {removed_value}") 
my_list.print_values() 

my_list.remove_val(17)
my_list.print_values() 

my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.insert_at(0, 0) 
my_list.insert_at(4, 4) 
my_list.insert_at(2.5, 3) 
my_list.print_values() 