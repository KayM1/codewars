class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return self.val
    
    def set_next(self, node):
        self.next = node                # .next is a quality of the node

class LLQueue:
    def __init__(self):
        self.tail = None
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " >> ".join(nodes)
    
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node) # self.tail.next = node -- self.tail.next = node (tell the tail that the next node is node)
            self.tail = node # the new node has now become the tail, so represent this

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head) # tell the node that the next node is self.head
            self.head = node # the new node has now become the head


