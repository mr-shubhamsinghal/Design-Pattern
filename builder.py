"""
Creational Design Pattern - Builder
"""
from abc import ABC, abstractmethod


class IBurger(ABC):
    @abstractmethod
    def set_lattice(self):
        pass

    @abstractmethod
    def set_patti(self):
        pass

class Burger(IBurger):
    def __init__(self):
        self.lattice = False
        self.patti = False

    def set_lattice(self):
        self.lattice = True
    
    def set_patti(self):
        self.patti = True

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
    
    def add_lattice(self):
        self.burger.set_lattice()
        return self
    
    def add_patti(self):
        self.burger.set_patti()
        return self
    
    def build(self):
        return self.burger

builder = BurgerBuilder()
print(builder.burger.patti)
print(builder.add_lattice().add_patti().build())
print(builder.burger.patti)