class pokeMoches:
    def __init__(self, name, max_hp, defence, speed, attacks):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attacks = attacks
        self.defence = defence
        self.speed = speed

    def decrease_hp(self, hp):
        self.current_hp -= hp

    def heal(self, hp=None):
        if hp is None:
            self.current_hp = self.max_hp
        else:
            self.current_hp += hp

    def print_hp(self):
        print(f"{self.name}'s HP: {self.current_hp}/{self.max_hp}")
