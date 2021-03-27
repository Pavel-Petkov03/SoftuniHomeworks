from Programming_OOP_with_Python.difining_classes_exercise.guild_system.project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.list_of_players.append(player)
            return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str):
        f = [p for p in self.list_of_players if p.name == player_name]
        if not f:
            return f"Player {player_name} is not in the guild."
        else:
            self.list_of_players.remove(f[0])
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            result += p.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())




