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

class Player(Player_BASE):
    pass

class AI_Player(Player_BASE):
    pass