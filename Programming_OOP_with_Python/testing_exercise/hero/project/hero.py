class Hero:
    username: str
    health: float
    damage: float
    level: int

    def __init__(self, username: str, level: int, health: float, damage: float):
        self.username = username
        self.level = level
        self.health = health
        self.damage = damage

    def battle(self, enemy_hero):
        if enemy_hero.username == self.username:
            raise Exception("You cannot fight yourself")

        if self.health <= 0:
            raise ValueError("Your health is lower than or equal to 0. You need to rest")

        if enemy_hero.health <= 0:
            raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")

        player_damage = self.damage * self.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level

        self.health -= enemy_hero_damage
        enemy_hero.health -= player_damage

        if self.health <= 0 and enemy_hero.health <= 0:
            return "Draw"

        if enemy_hero.health <= 0:
            self.level += 1
            self.health += 5
            self.damage += 5
            return "You win"

        enemy_hero.level += 1
        enemy_hero.health += 5
        enemy_hero.damage += 5
        return "You lose"

    def __str__(self):
        return f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.h = Hero('name', 1, 20, 40)
        self.new_h = Hero('new_name', 1, 40, 60)

    def test__init__data(self):
        name = 'name'
        level = 1
        health = 20
        damage = 40
        self.assertEqual(name, self.h.username)
        self.assertEqual(level, self.h.level)
        self.assertEqual(health, self.h.health)
        self.assertEqual(damage, self.h.damage)

    def test_battle_taken_object_username_equals_instance_username__expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.new_h.username = 'name'
            self.h.battle(self.new_h)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_instance_health_less_or_equal_to_zero_expected_value_error(self):
        with self.assertRaises(ValueError)as ex:
            self.h.health = 0
            self.h.battle(self.new_h)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_object_health_less_than_zero_expected_value_error(self):
        with self.assertRaises(ValueError)as ex:
            self.new_h.health = 0
            self.h.battle(self.new_h)
        self.assertEqual(f"You cannot fight {self.new_h.username}. He needs to rest", str(ex.exception))

    def test_both_players_under_zero_health_expected_draw(self):
        self.h.health = 60
        actual = self.h.battle(self.new_h)
        self.assertEqual(actual, 'Draw')

    def test_object_hero_lost_expected_you_win(self):
        self.h.health = 100
        expected_new_level = 2
        expected_new_health = 45
        expected_new_damage = 45
        actual = self.h.battle(self.new_h)
        self.assertEqual(actual, 'You win')
        self.assertEqual(expected_new_health, self.h.health)
        self.assertEqual(expected_new_damage, self.h.damage)
        self.assertEqual(expected_new_level, self.h.level)


    def test_instance_hero_lost_expected_you_loose(self):
        self.new_h.health = 100
        actual = self.h.battle(self.new_h)
        expected_new_level = 2
        expected_new_health = 65
        expected_new_damage = 65
        self.assertEqual(actual, 'You lose')
        self.assertEqual(expected_new_health, self.new_h.health)
        self.assertEqual(expected_new_damage, self.new_h.damage)
        self.assertEqual(expected_new_level, self.new_h.level)

    def test_str_method(self):
        expected = f"Hero {self.h.username}: {self.h.level} lvl\n" \
               f"Health: {self.h.health}\n" \
               f"Damage: {self.h.damage}\n"
        actual = str(self.h)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()