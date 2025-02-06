import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 5
        self.happiness = 50
        self.satiety = 10
        self.weekday = ["Старт","Понеділок","Вівторок","Середа","Четвер","П'ятниця","Субота","Неділя"]
        self.current_day_index = 1
        self.current_day = self.weekday[self.current_day_index]
        self.job = "Нема"
        self.car = "Нема"
        self.house = "Нема"

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

    def work(self):
        self.money += self.job.salary
        self.happiness -= 10
        self.satiety -= 8
        print(f"{self.name} працював і заробив {self.job.salary}. Баланс: {self.money}.")

    def simulate_day(self):
        self.house.mess += random.randint(5, 10)

        if self.satiety < 20:
            self.eat()

        elif self.job == "Нема":
            random_job = random.randint(1, 3)
            if random_job == 1:
                self.get_job(Job("Прибиральник", 20, 10))
            elif random_job == 2:
                self.get_job(Job("Офісний працівник", 30, 5))
            elif random_job == 3:
                self.get_job(Job("Начальник", 50, 2))

        elif self.current_day not in ["Субота", "Неділя"]:
            self.work()


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

for day in range(1, 10):
    print(f"\nДень {day}")
    print(f"Сьогодні {human.current_day}")
    if human.current_day_index == 7:
        human.current_day_index = 1
        human.current_day = human.weekday[human.current_day_index]
        human.simulate_day()
    else:
        human.current_day_index += 1
        human.current_day = human.weekday[human.current_day_index]
        human.simulate_day()