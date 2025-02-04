import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 50
        self.job = None
        self.car = None
        self.house = None

class Auto:
    def __init__(self, brand, fuel, durability, fuel_consumption):
        self.brand = brand
        self.fuel = fuel
        self.durability = durability
        self.fuel_consumption = fuel_consumption

class House:
    def __init__(self):
        self.mess = 0
        self.food = 5

class Job:
    def __init__(self, position, salary, happiness_loss):
        self.position = position
        self.salary = salary
        self.happiness_loss = happiness_loss

