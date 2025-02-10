import random

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 5
        self.happiness = 50
        self.satiety = 10
        self.alive = True
        self.work_today = False
        self.weekday = ["Старт", "Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        self.current_day_index = 1
        self.current_day = self.weekday[self.current_day_index]
        self.job = "Нема"
        self.car = "Нема"
        self.house = "Нема"

    def get_job(self, job="Нема"):
        self.satiety -= 10
        random_job = random.randint(1, 5)
        if random_job == 1:
            random_job = random.randint(1, 3)
            if random_job == 1:
                job = Job("Прибиральник", 20, 10)
            elif random_job == 2:
                job = Job("Офісний працівник", 30, 5)
            elif random_job == 3:
                job = Job("Начальник", 50, 2)
            self.job = job
            print(f"{self.name}отримав роботу: {job.position}")
        else:
            print(f"{self.name}не знайшов роботу")

    def buy_food(self):
       if self.money >= 10:
           house.food += random.randint(1, 5)
           self.money -= random.randint(10, 20)
           print(f"{self.name}купив їжу. Їжі вдома: {house.food}.")
           human.simulate_day()
       else:
           print(f"{self.name}не вистачає грошей на їжу!")
           self.happiness += 20
           human.simulate_day()

    def eat(self):
        if house.food > 0:
            self.satiety += random.randint(20, 40)
            max_eat_food = random.randint(1, 4)
            if max_eat_food > house.food:
                house.food -= house.food
                print(f"{self.name}поїв. Ситість: {self.satiety} Їжі вдома: {house.food}")
                if house.food <= 1:
                    self.buy_food()
                human.simulate_day()
            else:
                house.food -= max_eat_food
                print(f"{self.name}поїв. Ситість: {self.satiety} Їжі вдома: {house.food}")
                if house.food <= 1:
                    self.buy_food()
                human.simulate_day()
        else:
            print("Немає їжі вдома")
            self.buy_food()

    def work(self):
        self.money += self.job.salary
        self.happiness -= 10
        self.satiety -= 10
        self.work_today = True
        print(f"{self.name}працював і заробив {self.job.salary}. Баланс: {self.money}, Ситість: {self.satiety}, Щастя: {self.happiness}")

    def have_fun(self):
        vacation_type = random.randint(1, 2)
        if vacation_type == 1:
            print(f"{self.name}захотів пограти в доту")
            if random.randint(1, 2) == 2:
                self.happiness += 10
                print(f"{self.name}він програв... Щастя: {self.happiness}")
            else:
                self.happiness += 20
                print(f"{self.name}він переміг! Щастя: {self.happiness}")
        else:
            self.happiness += 20
            print(f"{self.name}відпочиває. Щастя: {self.happiness}")

    def clean_house(self):
        if self.house:
            self.house.mess = 0
            self.happiness += 10
            print(f"{self.name} прибрав у домі. Щастя: {self.happiness}")

    def get_car(self):
        pass

    def simulate_day(self):
        if self.happiness < 1:
            self.alive = False
        else:
            self.house.mess += random.randint(5, 10)
            if self.satiety < 20:
                self.eat()
            elif self.job == "Нема":
                self.get_job()
            elif self.current_day not in ["Субота", "Неділя"] and not self.work_today:
                self.work()
            elif self.current_day in ["Субота", "Неділя"]:
                if house.mess > 60:
                    self.clean_house()
                else:
                    self.have_fun()

class Auto:
    def __init__(self, brand, fuel, durability, fuel_consumption):
        self.brand = brand
        self.fuel = fuel
        self.durability = durability
        self.fuel_consumption = fuel_consumption

class House:
    def __init__(self):
        self.mess = 0
        self.food = 10

class Job:
    def __init__(self, position, salary, happiness_loss):
        self.position = position
        self.salary = salary
        self.happiness_loss = happiness_loss

human = Human("Віктор Коренеплід ")
house = House()
human.house = house

for day in range(1, 11):
    if human.alive:
        human.work_today = False
        print(f"\nДень: {day}")
        print(f"Сьогодні: {human.current_day}")

        print("\nСтатистика:\n")
        print(f"Ім'я: {human.name}")
        print(f"Гроші: {human.money}")
        print(f"Щастя: {human.happiness}")
        print(f"Ситість: {human.satiety}")
        print(f"Забруднення у квартирі: {house.mess}")
        print(f"Їжі у квартирі: {house.food}")
        print("\nРозпорядок для:\n")

        if human.current_day_index == 7:
            human.current_day_index = 1
            human.current_day = human.weekday[human.current_day_index]
            human.simulate_day()
        else:
            human.current_day_index += 1
            human.current_day = human.weekday[human.current_day_index]
            human.simulate_day()
    else:
        print(f"{human.name}загинув...")
        break