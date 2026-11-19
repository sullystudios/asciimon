import unittest
from asciimon_game.ui import hp_bar, ask_choice, ask_text
from unittest.mock import patch


class Test(unittest.TestCase):

    def test_hp_bar_1(self):
        self.assertEqual(hp_bar(14, 20), "[#######---]")
    
    def test_hp_bar_2(self):
        self.assertEqual(hp_bar(20, 20), "[##########]")
   
    def test_hp_bar_3(self):
        self.assertEqual(hp_bar(0, 20), "[----------]")
   
    def test_hp_bar_4(self):
        self.assertEqual(hp_bar(1, 20), "[#---------]")
   
    def test_hp_bar_5(self):
        self.assertEqual(hp_bar(19, 20), "[#########-]")

    def test_ask_choice(self):
        with patch("builtins.input", side_effect=["abc", "0", "9", "", "2"]):
            result = ask_choice("Pick", ["A", "B", "C"])
        self.assertEqual(result, 1)

    def test_ask_text1(self):
        with patch("builtins.input", side_effect=["", "    ", "Jacob"]):
            result = ask_text("What's your name?")
        self.assertEqual(result, "Jacob")
   
    def test_ask_text2(self):
        with patch("builtins.input", side_effect=["ThisNameIsWayTooLong", "Ash"]):
            result = ask_text("What's your name?")
        self.assertEqual(result, "Ash")
    
    def test_ask_text3(self):
        with patch("builtins.input", side_effect=[""]):
                result = ask_text("Nickname?", allow_blank=True)
        self.assertEqual(result, "")