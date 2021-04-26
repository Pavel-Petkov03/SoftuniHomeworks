from project.hero import Hero

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
        self.assertEqual(f"You cannot fight name. He needs to rest", str(ex.exception))
        self.assertEqual(self.another_hero.health, -5)

    def test_another_hero_object_health_less_than_zero__expected_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.another_hero.health = 0
            self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(f"You cannot fight name. He needs to rest", str(ex.exception))
        self.assertEqual(self.another_hero.health, 0)

    def test_both_heroes_under_or_equal_to_zero_expected_draw(self):
        result = self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(result, 'Draw')
        self.assertTrue(self.my_instance_hero.health <= 0 and self.another_hero.health <= 0)

    def test_instance_hero_win(self):
        self.another_hero.damage = 1
        result = self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(result, 'You win')
        self.assertEqual(self.my_instance_hero.health, 95)
        self.assertEqual(self.my_instance_hero.damage, 25)
        self.assertEqual(self.my_instance_hero.level, 2)

    def test_instance_hero_lose(self):
        self.another_hero.health = 1000
        result = self.my_instance_hero.battle(self.another_hero)
        self.assertEqual(result, 'You lose')
        self.assertEqual(self.another_hero.health, 985)
        self.assertEqual(self.another_hero.damage, 35)
        self.assertEqual(self.another_hero.level, 11)

    def test_str_method(self):
        massive = self.my_instance_hero.__str__().split('\n')
        self.assertEqual(massive[0], f"Hero username: 1 lvl")
        self.assertEqual(massive[1], f"Health: 100")
        self.assertEqual(massive[2], f"Damage: 20")


if __name__ == "__main__":
    unittest.main()
