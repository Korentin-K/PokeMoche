class PokeMoche:
    name: str
    level: int
    attack: int
    specialAttack: int
    defence: int
    specialDefence: int
    speed: int

    def __init__(self, name="", level=1, attack=0, specialAttack=0, defence=0, specialDefence=0, speed=0):
        self._name = name
        self._level = level
        self._attack = attack
        self._specialAttack = specialAttack
        self._defence = defence
        self._specialDefence = specialDefence
        self._speed = speed

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def attack(self):
        return self._attack

    @property
    def specialAttack(self):
        return self._specialAttack

    @property
    def defence(self):
        return self._defence

    @property
    def specialDefence(self):
        return self._specialDefence

    @property
    def speed(self):
        return self._speed

    @name.setter
    def name(self, value):
        self._name = value

    @level.setter
    def level(self, value):
        self._level = value

    @attack.setter
    def attack(self, value):
        self._attack = value

    @specialAttack.setter
    def specialAttack(self, value):
        self._specialAttack = value

    @defence.setter
    def defence(self, value):
        self._defence = value

    @specialDefence.setter
    def specialDefence(self, value):
        self._specialDefence = value

    @speed.setter
    def speed(self, value):
        self._speed = value
