import unittest
from asciimon_game.moves import type_multi

class Test(unittest.TestCase):

    def test_fire_beats_grass(self):
        self.assertEqual(type_multi("Fire", "Grass"), 2.0)

    def test_fire_resists_grass(self):
        self.assertEqual(type_multi("Grass", "Fire"), 0.5)

    def test_water_beats_fire(self):
        self.assertEqual(type_multi("Water", "Fire"), 2.0)

    def test_water_resists_fire(self):
        self.assertEqual(type_multi("Fire", "Water"), 0.5)

    def test_grass_beats_water(self):
        self.assertEqual(type_multi("Grass", "Water"), 2.0)

    def test_normal_equals_water(self):
        self.assertEqual(type_multi("Normal", "Water"), 1.0)

    def test_fire_equals_fire(self):
        self.assertEqual(type_multi("Fire", "Fire"), 1.0)
        