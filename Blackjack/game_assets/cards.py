class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
   
    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"

    def __repr__(self):
        return self.__name

class Deck:
    def __init__(self):
        self.__cards = []
        self.create()
    
    def create(self):
        pass
    
    def __str__(self):
        return str(self.__cards)


if __name__ == "__main__":
    suits = ["Heart ♥", "Club ♣", "Diamond ♦", "Spade ♠"]

    deck = Deck()
    print(deck)