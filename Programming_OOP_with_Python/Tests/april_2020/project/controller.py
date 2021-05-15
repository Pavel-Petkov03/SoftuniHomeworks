from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.battle_field import BattleField


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type_, username):
        p = None
        if type_ == 'Advanced':
            p = Advanced(username)
        elif type_ == 'Beginner':
            p = Beginner(username)
        self.player_repository.add(p)
        return f"Successfully added player of type {type_} with username: {username}"

    def add_card(self, type_, name):
        c = None
        if type_ == 'Magic':
            c = MagicCard(name)
        elif type_ == 'Trap':
            c = TrapCard(name)
        self.card_repository.add(c)
        return f"Successfully added card of type {type_}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = []
        for p in self.player_repository.players:
            result.append(f'Username: {p.username} - Health: {p.health} - Cards {len(p.card_repository.cards)}')
            for c in p.card_repository.cards:
                result.append(f'### Card: {c.name} - Damage: {c.damage_points}')
        result = '\n'.join(result)
        result += '\n'
        return result


co = Controller()
b = Beginner('aa')
b.card_repository.cards = [MagicCard('aa'), TrapCard('bb')]
co.player_repository.players = [b, Advanced('bb')]
print(co.report())