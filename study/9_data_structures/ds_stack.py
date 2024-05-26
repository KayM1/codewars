# stack

import random #to shuffle

class Stack:
    def __init__(self):
        self.cards = []
    
    def push(self, card):
        self.cards.append(card)
    
    def pop(self): # we add functionality here in case of empty class / stack to avoid errors
        if len(self.cards) == 0:
            return None
        removed_card = self.cards.pop()
        print(f"We're removing: '{removed_card}' from the deck.")
        return removed_card
    
    def peek(self):
        if len(self.cards) == 0:
            return None
        return self.cards[len(self.cards) - 1]
    
    def size(self):
        return len(self.cards)
    
    ## end of stack study

    def generate_deck(self):
        list_types = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        list_values = [ 'One', 'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Peasant','Queen','King','Joker']
        last_super = ['First Deck','Second Deck','Third Deck']
        
        for super in last_super:
            for type in list_types:
                for value in list_values:
                    # self.cards.append(f"{super}: {value} of {type}")
                    self.cards.append(f"{value} of {type}")

        return("# Deck generated.")

    def shuffle(self):
        random.shuffle(self.cards)

    def show_deck(self):
        print("## Showing the deck: ")
        counter = 1
        for card in self.cards:
            print(f"{card}")
            counter += 1

def main():
    DeckofCards = Stack()
    DeckofCards.generate_deck()
    DeckofCards.shuffle()
    DeckofCards.show_deck()
     
    # print(DeckofCards)

main()

