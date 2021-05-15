from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        [self.__beginner_bonus(b) for b in [attacker, enemy] if isinstance(b, Beginner)]
        [self.__get_bonus_health(p) for p in [attacker, enemy]]
        for card in attacker.card_repository:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                enemy.re
                return
        for card in enemy.card_repository:
            attacker.take_damage(card.damage_points)
            if attacker.is_dead:
                return

    @staticmethod
    def __beginner_bonus(beginner: Beginner):
        beginner.health += 40
        beginner.card_repository.cards = [card.damage_points + 30 for card in beginner.card_repository.cards]

    @staticmethod
    def __get_bonus_health(player: Player):
        for p in player.card_repository:
            player.health += p.health_points
