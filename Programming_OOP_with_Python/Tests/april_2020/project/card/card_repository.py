class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add_card(self, card):
        initial = [c for c in self.cards if c.name == card.name]
        if initial:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        p = self.find(card)
        self.cards.remove(p)
        self.count -= 1

    def find(self, name):
        return [c for c in self.cards if c.name == name][0]
