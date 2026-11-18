from asciimon_game.data import SPECIES

class Creature:
    def __init__(self, species, level, nickname=None):
        self.species = species
        self.level = level
        self.nickname = nickname
        if nickname:
            self.name = nickname
        else:
            self.name = species
        base = SPECIES[species]
        self.type = base["type"]
        self.moves = base["moves"]
        self.update_stats()
        self.hp = self.max_hp
        self.xp = 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        
    def is_fainted(self):
        return self.hp == 0

    def heal(self, amount=None):
        if amount == None:
            self.hp = self.max_hp
        else:
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

    def update_stats(self):
        base = SPECIES[self.species]
        self.max_hp = base["base_hp"] + self.level * 2
        self.attack = base["base_attack"] + self.level
        self.defense = base["base_defense"] + self.level
        self.speed = base["base_speed"] + self.level
    
    def gain_xp(self, amount):
        self.xp += amount
        needed_xp = self.level * 10
        if self.xp >= needed_xp:
            self.xp -= needed_xp
            damage = self.max_hp - self.hp
            self.level += 1
            self.update_stats()
            self.hp = self.max_hp - damage
            return True
        return False

    def to_dict(self):
        return {
            "species": self.species,
            "nickname": self.nickname,
            "level": self.level,
            "xp": self.xp,
            "hp": self.hp
        }

    @classmethod
    def from_dict(cls, data):
        mon = cls(data["species"], data["level"], data["nickname"])
        mon.hp = data["hp"]
        mon.xp = data["xp"]
        return mon