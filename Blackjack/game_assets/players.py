import random

class Player_BASE:
    def __init__(self):
        # First: define attributes
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        # Then: call methods
        self.create()

    def create(self):
        self.__name = self.get_random_name()
        self.__credits = random.randint(20, 100)

    def get_random_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def init_hand(self, deck):
        self.__hand.clear()
        self.__hand.append(deck.draw())

        # get new card
        self.add_card(deck.draw())

    def add_card(self, new_card):
        # check hand value
        if self.hand_value > 10 and new_card.value == 11:
            new_card.value = 1
        
        self.__hand.append(new_card)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def credits(self):
        return self.__credits

    @property
    def hand_value(self):
        hand_value = 0
        for card in self.__hand:
            hand_value += card.value
        
        # list comprehension
        # hand_value = sum([card.value for card in self.__hand])
        
        return hand_value

    def __str__(self):
        return f"{self.__name} Credits: {self.__credits} Hand: {self.__hand} Hand Value {self.hand_value}"




class Player(Player_BASE):
    # partial override on create()
    def create(self):
        super().create()
        self.name = "Robert Vari"

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    from cards import Deck
    deck = Deck()
    player = Player()
    ai_player = AI_Player()

    # start game
    player.init_hand(deck)
    ai_player.init_hand(deck)

    # start rounds
    player.draw(deck)
    ai_player.draw(deck)

    # print player stats
    print(player)
    print(ai_player)