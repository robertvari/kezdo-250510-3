import random, time

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
        self.__playing = True
        self.__hand.append(deck.draw())

        # get new card
        self.add_card(deck.draw())

    def add_card(self, new_card):
        # check hand value
        if self.hand_value > 10 and new_card.value == 11:
            new_card.value = 1
        
        self.__hand.append(new_card)

    def draw(self, deck):
        while self.__playing:
            if self.hand_value <= 16:
                print(f"{self.name} draws a card...")
                time.sleep(2)

                new_card = deck.draw()
                self.add_card(new_card)
            else:
                print(f"{self.name} finishes.")
                self.__playing = False

    def add_credits(self, credits):
        self.__credits += credits
        print(f"{self.name} get {credits}")

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

    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_playing):
        self.__playing = new_playing

    @property
    def hand(self):
        return tuple(self.__hand)

    def __str__(self):
        return f"{self.__name} Credits: {self.__credits} Hand: {self.__hand} Hand Value {self.hand_value}"

    def __repr__(self):
        return self.name



class Player(Player_BASE):
    # partial override on create()
    def create(self):
        super().create()
        self.name = "Robert Vari"
    
    def draw(self, deck):
        print(f"This is your turn {self.name}")

        while self.playing:
            if self.hand_value > 21:
                print("Your hand valu is greater than 21")
                self.playing = False
                break

            print(f"Your cards: {self.hand} Value: {self.hand_value}")
            response = input("Do you want to draw a new card? (y/n)")
            if response == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")
                self.add_card(new_card)
            else:
                self.playing = False

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
    ai_player.draw(deck)
    player.draw(deck)

    # print player stats
    print(player)
    print(ai_player)