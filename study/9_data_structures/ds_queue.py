class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)  # insert at the end of the queue

    def pop(self, item):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    

# def push(self, item):
#   self.items.inser(0, item)