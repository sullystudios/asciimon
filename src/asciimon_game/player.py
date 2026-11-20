class Player:
    def __init__(self, name):
        self.name = name
        self.party = []
        self.items = {"ball": 5, "potion": 2}
        self.area = "town"
        self.beaten = set()

    def first_healthy(self):
        for creature in self.party:
            if not creature.is_fainted():
                return creature
        return None

    def heal_party(self):
        for creature in self.party:
            creature.heal()

    def all_fainted(self):
        return self.first_healthy() is None