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
    pass


if __name__ == "__main__":
    suits = ["Heart ♥", "Club ♣", "Diamond ♦", "Spade ♠"]

    card1 = Card("♠ Ace", 11)
    card2 = Card("♣ King", 10)
    card3 = Card("♦ Queen", 10)
    
    deck = [card1, card2, card3]
    print(deck)