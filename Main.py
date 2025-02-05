import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 5
        self.happiness = 50
        self.satiety = 10
        self.job = None
        self.car = None
        self.house = None

    def get_job(self, job):
        self.job = job
        print(f"{self.name} отримав роботу: {job.position}")

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


    def simulate_day(self):
        if self.satiety < 20:
            self.eat()
        elif not self.job:
            random_job = random.randint(1, 3)
            if random_job == 1:
                self.get_job(Job("Прибиральник", 20, 10))
                return self
            elif random_job == 2:
                self.get_job(Job("Офісний працівник", 30, 5))
                return self
            elif random_job == 3:
                self.get_job(Job("Начальник", 50, 2))
                return self

        elif self.money < 10:
            self.work()


    def work(self):
         self.money += self.job.salary
         self.happiness -= 10
         self.satiety -= 8
         print(f"{self.name} працював і заробив {self.job.salary}. Баланс: {self.money}.")


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

print(f"\nДень 1:\n")
human.simulate_day()

print(f"\nДень 2:\n")
human.simulate_day()

print(f"\nДень 3:\n")
human.simulate_day()