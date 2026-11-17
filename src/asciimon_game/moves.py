STRONG_AGAINST = {
    "Fire": "Grass",
    "Water": "Fire",
    "Grass": "Water"
}

MOVES = {
    "Ember": {"type": "Fire", "power": 8},
    "Fire Punch": {"type": "Fire", "power": 10},
    "Flamethrower": {"type": "Fire", "power": 15},
    "Water Gun": {"type": "Water", "power": 8},
    "Bubble": {"type": "Water", "power": 10},
    "Hydro Pump": {"type": "Water", "power": 15},
    "Absorb": {"type": "Grass", "power": 8},
    "Vine Whip": {"type": "Grass", "power": 10},
    "Razor Leaf": {"type": "Grass", "power": 15},
    "Tackle": {"type": "Normal", "power": 5},
    "Quick Attack": {"type": "Normal", "power": 8},
    "Slash": {"type": "Normal", "power": 10}
}

def type_multi(move_type, defender_type):
    if STRONG_AGAINST.get(move_type) == defender_type:
        return 2.0
    if STRONG_AGAINST.get(defender_type) == move_type:
        return 0.5
    return 1.0