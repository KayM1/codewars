import random

class Stack:
    def __init__(self):
        self.cards = []         # we're setting up a stack as a list

    def push(self, card):       # we're adding a card to the list
        self.cards.append(card)

    def pop(self):
        if len(self.cards) == 0: # we're catching an error, else we're popping
            return None
        return self.cards.pop()
    
    def peek(self):
        if len(self.cards) == 0: # error catching
            return None
        return self.cards[len(self.cards) - 1]
    
    def size(self):
        return len(self.cards)


class Stacks:
    def __init__(self):
        self.cards = []

    def push(self, card):
        self.cards.append(card)

    def pop(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def peek(self):
        if len(self.cards) == 0:
            return None
        return self.cards[len(self.cards) - 1]
    
    def size(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)