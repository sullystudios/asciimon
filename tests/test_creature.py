import unittest
from asciimon_game.creature import Creature

class TestCreature(unittest.TestCase):

    def setUp(self):
        self.mon = Creature("Embark", 5)

    def test_start_full_hp(self):
        self.assertEqual(self.mon.hp, self.mon.max_hp)

    def test_no_nickname_uses_species(self):
        self.assertEqual(self.mon.name, "Embark")

    def test_nickname_used_as_name(self):
        mon = Creature("Embark", 5, "Blaze")
        self.assertEqual(mon.name, "Blaze")

    def test_damage_no_0(self):
        self.mon.take_damage(999)
        self.assertEqual(self.mon.hp, 0)

    def test_faint_at_0(self):
        self.mon.take_damage(999)
        self.assertTrue(self.mon.is_fainted())

    def test_full_heal(self):
        self.mon.take_damage(10)
        self.mon.heal()
        self.assertEqual(self.mon.hp, self.mon.max_hp)

    def test_heal_not_above_max(self):
        self.mon.take_damage(2)
        self.mon.heal(5)
        self.assertEqual(self.mon.hp, self.mon.max_hp)

    def test_level_up(self):
        leveled = self.mon.gain_xp(50)
        self.assertTrue(leveled)
        self.assertEqual(self.mon.level, 6)

    def test_save_round_trip(self):
        self.mon.take_damage(5)
        self.mon.gain_xp(7)
        copy = Creature.from_dict(self.mon.to_dict())
        self.assertEqual(copy.species, self.mon.species)
        self.assertEqual(copy.level, self.mon.level)
        self.assertEqual(copy.hp, self.mon.hp)
        self.assertEqual(copy.xp, self.mon.xp)
        self.assertEqual(copy.nickname, self.mon.nickname)