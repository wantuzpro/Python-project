import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 10
        self.job = None
        self.car = None
        self.house = None

    def simulate_day(self):
        if self.satiety < 20:
            self.eat()

    def eat(self):
        if self.house.food > 0:
            self.satiety += random.randint(30, 70)
            self.house.food -= random.randint(1, 4)
            print(f"{self.name} поїв. Ситість: {self.satiety}. Їжі вдома: {self.house.food}")
        else:
            print("Немає їжі вдома")
            self.buy_food()

    def buy_food(self):
       if self.money >= 10:
           self.house.food += random.randint(1, 5)
           self.money -= random.randint(10, 20)
           print(f"{self.name} купив їжу. Їжі вдома: {self.house.food}.")
       else:
           print(f"{self.name} не вистачає грошей на їжу!")


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


human = Human("Андрій")
house = House()
human.house = house

print(f"\nДень 1:")
human.simulate_day()
