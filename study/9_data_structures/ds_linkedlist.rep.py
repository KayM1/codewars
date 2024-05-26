# set up the node o_
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return self.val
    
    def set_next(self, node):
        self.next = node

# set up the linked list o_o_o_
class LinkedList:
    def __init__(self): # _x
        self.head = None
    
    def __iter__(self):    # we must assume that linkedlist has nodes with .next properties underneath it
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):  # we're trying to catch as many errors as possible
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
    
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def add_to_head(self, node): # this can exist in a linked list, but should not be present in a linked list queue, since queues only add to the tail
        if self.head  == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

# functionality, how to turn it into a normal list, how to get last node
def turn_linkedlist_to_list(linkedlist):
    list = []
    for node in linkedlist:
        list.append(node.val) # append the value, not the object!
    return list
 
def get_last_node(linkedlist):
    current = linkedlist.head
    while hasattr(current, "val") and current.next:
        current = current.next
    return current

list_of_items = ["Sword", "Dagger", "Shield", "Potion"]

def main():
    linked_list = LinkedList()
    for item in list_of_items:
        linked_list.add_to_tail(Node(item))
    print(linked_list)

    list_result = turn_linkedlist_to_list(linked_list)
    print("Linked list to list:", list_result)

    last_node = get_last_node(linked_list)
    print("Last node:", last_node)  # Should print the last node

main()

