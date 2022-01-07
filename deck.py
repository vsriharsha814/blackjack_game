import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        for x in range(1, 14):
            for y in range(4):
                self.cards.append(Card(x, y))
    
    def draw(self, iteration):
        cards = []
        for x in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)