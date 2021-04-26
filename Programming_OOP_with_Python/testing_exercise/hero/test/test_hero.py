from hero.project.hero import Hero

import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.my_instance_hero = Hero('username', 1, 100, 20)
        self.another_hero = Hero('name', 10, 20, 30)

    def test__init__hero(self):
        self.assertEqual(self.my_instance_hero.username, 'username')
        self.assertEqual(self.my_instance_hero.level, 1)
        self.assertEqual(self.my_instance_hero.damage, 20)
        self.assertEqual(self.my_instance_hero.health, 100)

    """
    test battle function cases
    """

    def test_both_objects_with_same_name__expected_exception(self):
        self.my_instance_hero.username = 'name'
        with self.assertRaises(Exception) as ex:
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_instance_hero_health_less_than__zero__expected_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.my_instance_hero.health = -5
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))
        self.assertEqual(self.my_instance_hero.health, -5)

    def test_instance_hero_health_equal_to_zero__expected_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.my_instance_hero.health = 0
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))
        self.assertEqual(self.my_instance_hero.health, 0)

    def test_another_hero_health_equal_to_zero_expected_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.another_hero.health = -5
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(f"You cannot fight {self.another_hero.username}. He needs to rest", str(ex.exception))
        self.assertEqual(self.another_hero.health, -5)

    def test_another_hero_object_health_less_than_zero__expected_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.another_hero.health = 0
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(f"You cannot fight {self.another_hero.username}. He needs to rest", str(ex.exception))
        self.assertEqual(self.another_hero.health, 0)

    def test_both_heroes_under_or_equal_to_zero_expected_draw(self):
        result = self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(result, 'Draw')

    def test_instance_hero_win(self):
        self.another_hero.damage = 1
        result = self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(result, 'You win')
        self.assertEqual(self.my_instance_hero.health, 95)
        self.assertEqual(self.my_instance_hero.damage, 25)
        self.assertEqual(self.my_instance_hero.level, 2)

    def test_instance_hero_lose(self):
        self.another_hero.health = 1000


# class TestHero(unittest.TestCase):
#     def setUp(self):
#         self.h = Hero('name', 1, 20, 40)
#         self.new_h = Hero('new_name', 1, 40, 60)
#
#     def test__init__data(self):
#         name = 'name'
#         level = 1
#         health = 20
#         damage = 40
#         self.assertEqual(name, self.h.username)
#         self.assertEqual(level, self.h.level)
#         self.assertEqual(health, self.h.health)
#         self.assertEqual(damage, self.h.damage)
#
#     def test_battle_taken_object_username_equals_instance_username__expected_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.new_h.username = 'name'
#             self.h.battle(self.new_h)
#         self.assertEqual("You cannot fight yourself", str(ex.exception))
#
#     def test_battle_instance_health_less_or_equal_to_zero_expected_value_error(self):
#         with self.assertRaises(ValueError)as ex:
#             self.h.health = 0
#             self.h.battle(self.new_h)
#         self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))
#
#     def test_battle_object_health_less_than_zero_expected_value_error(self):
#         with self.assertRaises(ValueError)as ex:
#             self.new_h.health = 0
#             self.h.battle(self.new_h)
#         self.assertEqual(f"You cannot fight {self.new_h.username}. He needs to rest", str(ex.exception))
#
#     def test_both_players_under_zero_health_expected_draw(self):
#         self.h.health = 60
#         actual = self.h.battle(self.new_h)
#         self.assertEqual(actual, 'Draw')
#
#     def test_object_hero_lost_expected_you_win(self):
#         self.h.health = 100
#         expected_new_level = 2
#         expected_new_health = 45
#         expected_new_damage = 45
#         actual = self.h.battle(self.new_h)
#         self.assertEqual(actual, 'You win')
#         self.assertEqual(expected_new_health, self.h.health)
#         self.assertEqual(expected_new_damage, self.h.damage)
#         self.assertEqual(expected_new_level, self.h.level)
#
#     def test_instance_hero_lost_expected_you_loose(self):
#         self.new_h.health = 100
#         actual = self.h.battle(self.new_h)
#         expected_new_level = 2
#         expected_new_health = 65
#         expected_new_damage = 65
#         self.assertEqual(actual, 'You lose')
#         self.assertEqual(expected_new_health, self.new_h.health)
#         self.assertEqual(expected_new_damage, self.new_h.damage)
#         self.assertEqual(expected_new_level, self.new_h.level)
#
#     def test_str_method(self):
#         expected = f"Hero {self.h.username}: {self.h.level} lvl\n" \
#                    f"Health: {self.h.health}\n" \
#                    f"Damage: {self.h.damage}\n"
#         actual = str(self.h)
#         self.assertEqual(expected, actual)
#
#
# if __name__ == "__main__":
#     unittest.main()
