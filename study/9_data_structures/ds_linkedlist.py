# creating a node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self): # overwrite the way it prints itself, instead of <object at 0azE87... gibberish> we make it return it's value
        return self.val
    
# creating LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):                 # this allows an object to be iterable, and how to be iterable
        current = self.head
        while current is not None:
            yield current
            current = current.next
    
    def __repr__(self): # how to print itself, as a linked list
        nodes = []
        current = self.head
        while current and hasattr(current, "val"): #important, else it might append None values
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
    
    def add_to_tail(self, node):
        self.head = node # simplified for now

# functionality, turning the LL into a normal list
def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)
    return result

# how to get last node
def get_last_node(linked_list):
    current = linked_list.head
    while hasattr(current, "val") and current.next:
        current = current.next
    return current

def main():
    passed = 0
    failed = 0
    linked_list = LinkedList()
    linked_list.add_to_tail(Node("Sword"))