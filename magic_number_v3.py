# compound class
class MagicNumber:
    def __init__(self):
        self.__player = Player()
        self.__computer = Computer()

    def start(self):
        print("-"*50, "MAGIC NUMBER", "-"*50)
        print(f"I think of a number between {self.__computer.min_number} and {self.__computer.max_number}. Can you guess it?")

class Player:
    pass

class Computer:
    def __init__(self):
        self.__min_number = 1
        self.__max_number = 10
    
    @property
    def min_number(self):
        return self.__min_number
    
    @property
    def max_number(self):
        return self.__max_number


my_game = MagicNumber()
my_game.start()