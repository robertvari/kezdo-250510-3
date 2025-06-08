class Player_BASE:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True


class Player(Player_BASE):
    pass

class AI_Player(Player_BASE):
    pass