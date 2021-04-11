class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        self.__name = new

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new):
        self.__rating = new

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, new):
        self.__players = new

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        initial_player = [p for p in self.__players if p.name == player_name]
        if not initial_player:
            return f"Player {player_name} not found"
        self.__players.remove(initial_player[0])
        return initial_player[0]
