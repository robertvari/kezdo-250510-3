class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"

class Deck:
    pass


if __name__ == "__main__":
    suits = ["Heart ♥", "Club ♣", "Diamond ♦", "Spade ♠"]

    card1 = Card("♠ Ace ♠", 11)
    card2 = Card("♣ King ♣", 10)
    card3 = Card("♦ Queen ♦", 10)
    print(card1)
    print(card2)
    print(card3)