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

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def credits(self):
        return self.__credits


    def create(self):
        self.__name = self.get_random_name()
        self.__credits = random.randint(20, 100)

    def get_random_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self):
        return f"{self.__name} Credits: {self.__credits} Hand: {self.__hand}"

class Player(Player_BASE):
    # partial override on create()
    def create(self):
        super().create()
        self.name = "Robert Vari"

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    ai_player = AI_Player()
    print(player)
    print(ai_player)