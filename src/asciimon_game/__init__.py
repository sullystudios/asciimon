from asciimon_game.player import Player
from asciimon_game.creature import Creature
from asciimon_game.battle import battle

def main() -> None:
    player = Player("Jake")
    player.party.append(Creature("Embark", 5))
    enemies = [Creature("Possnap", 5)]
    result = battle(player, enemies, wild=True)
    print(result)