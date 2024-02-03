from typing import List, Union, Optional
import PokeMoche


class Player:
    name: str
    badges: int
    nbPokemoches: int
    coins: int
    inventory: List[Union[str, int]]
    mocheDex: [PokeMoche]

    def __init__(self, name: str, badges: 0, nbPokemoches: 0, coins: 0, inventory: [], mocheDex: []):
        self.coins = coins
        self.name = name
        self.badges = badges
        self.nbPokemoches = nbPokemoches
        self.inventory = inventory
        self.mocheDex = mocheDex

    @property
    def name(self) -> str:
        return self.name

    @property
    def badges(self) -> int:
        return self.badges

    @property
    def nbPokemoches(self) -> int:
        return self.nbPokemoches

    @property
    def coins(self) -> int:
        return self.coins

    @property
    def inventory(self) -> List[Union[str, int]]:
        return self.inventory

    @name.setter
    def name(self, name: str) -> None:
        self.name = name

    @badges.setter
    def badges(self, badges: int) -> None:
        self.badges = badges

    @nbPokemoches.setter
    def nbPokemoches(self, nbPokemoches: int) -> None:
        self.nbPokemoches = nbPokemoches

    @coins.setter
    def coins(self, coins: int) -> None:
        self.coins = coins

    @inventory.setter
    def inventory(self, inventory: List[Union[str, int]]) -> None:
        self.inventory = inventory

    @mocheDex.setter
    def mocheDex(self, mocheDex: List[PokeMoche]) -> None:
        self.mocheDex = mocheDex
