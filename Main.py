import random
import os

class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 10
        self.alive = True
        self.work_today = False
        self.weekday = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        self.current_day_index = 0
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
                job = Job("Шеф", 50, 2)
            self.job = job
            print(f"{self.name}отримав роботу: {job.position}")
        else:
            print(f"{self.name}не знайшов роботу")

    def buy_food(self):
        products = random.randint(1, 5)
        price = random.randint(2, 5)
        price *= products

        if self.money >= price:
            house.food += products
            self.money -= price
            print(f"{self.name}купив їжу. Їжі вдома: {house.food}.")
            human.simulate_day()
        else:
            print(f"{self.name}не вистачає грошей на їжу!")
            self.happiness -= random.randint(5, 10)

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
                reason_losing = random.randint(1, 4)
                if reason_losing == 1:
                    self.happiness -= 10
                    print(f"Анти-маг зібрав бф на 40 хвилині. {self.name}програв... Щастя: {self.happiness}")
                elif reason_losing == 2:
                    self.happiness -= 5
                    print(f"Заруїнили агенти габена. {self.name}програв... Щастя: {self.happiness}")
                elif reason_losing == 3:
                    self.happiness -= 10
                    print(f"Керрі не натиснув бкб у файте. {self.name}програв... Щастя: {self.happiness}")
                else:
                    self.happiness += 10
                    print(f"{self.name}програв... Щастя: {self.happiness}")
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

    def buy_car(self):
        print("1. Nissan, ціна: 100, витрата палива: 60")
        print("2. BMW, ціна: 120, витрата палива: 40")
        print("3. Toyota, ціна: 240, витрата палива: 10")
        match input("Яку купити?: "):
            case "1":
                if self.money > 99:
                    self.car = Auto("Nissan", 0, 100, 60)
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case "2":
                if self.money > 119:
                    self.car = Auto("BMW", 0, 120, 40)
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case "3":
                if self.money > 239:
                    self.car = Auto("Toyota", 0, 240, 10)
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case _:
                print("Неправильний ввід")

    def check_status(self):
        self.house.mess += random.randint(5, 10)
        print("Події дня:")
        if self.happiness < 1:
            self.alive = False
        else:
            if self.satiety < 10:
                print(f"{self.name}зголоднів")
            elif self.job == "Нема":
                print(f"{self.name}безробітний")
            elif self.current_day not in ["Субота", "Неділя"] and not self.work_today:
                print(f"{self.name}потрібно сходити на роботу")
            elif self.current_day in ["Субота", "Неділя"]:
                print("сьогодні вихідні можна відпочити")
            elif house.mess > 60:
                print("У будинку брудно. Може варто прибрати?")

    def simulate_day(self):
        match input("Що робити?: "):
            case "1":
                if human.job == "Нема":
                    self.get_job()
                else:
                    if self.current_day not in ["Субота", "Неділя"] and not self.work_today:
                        self.work()
                    else:
                        print("Ви не можете працювати сьогодні")
            case "2":
                print(f"Купити: 1. Їжу, 2. Машину. Гроші: {human.money}")
                match input("Що купити?: "):
                    case "1":
                        self.buy_food()
                    case "2":
                        self.buy_car()
            case "3":
                self.eat()
            case "4":
                self.clean_house()
            case "5":
                self.have_fun()
            case _:
                print("Неправильний ввід")

class House:
    def __init__(self):
        self.mess = 0
        self.food = 10

class Job:
    def __init__(self, position, salary, happiness_loss):
        self.position = position
        self.salary = salary
        self.happiness_loss = happiness_loss

class Auto:
    def __init__(self, brand, fuel, durability, fuel_consumption):
        self.brand = brand
        self.fuel = fuel
        self.durability = durability
        self.fuel_consumption = fuel_consumption

human = Human("Віктор Коренеплід ")
house = House()
human.house = house

print("\nСтатистика:\n")
print(f"Ім'я: {human.name}")
print(f"Гроші: {human.money}")
print(f"Щастя: {human.happiness}")
print(f"Ситість: {human.satiety}")
print(f"Забруднення у квартирі: {house.mess}")
print(f"Їжі у квартирі: {house.food}")

for day in range(1, 21):
    if human.alive:
        human.work_today = False
        print(f"\nДень: {day}")
        print(f"Сьогодні: {human.current_day}")

        print(f"\nГроші: {human.money}, Щастя {human.happiness}, Ситість: {human.satiety}, Забруднення у квартирі: {house.mess}\n")

        if human.job == "Нема":
            print("1. Шукати роботу")
            print("2. Купити")
            print("3. Їсти")
            print("4. Прибрати в будинку")
            print("5. Відпочивати\n")
        else:
            print("1. Працювати")
            print("2. Купити")
            print("3. Їсти")
            print("4. Прибрати в будинку")
            print("5. Відпочивати\n")

        human.check_status()

        if human.current_day_index == 6:
            human.current_day_index = 0
            human.current_day = human.weekday[human.current_day_index]
            human.simulate_day()
        else:
            human.current_day_index += 1
            human.current_day = human.weekday[human.current_day_index]
            human.simulate_day()
    else:
        print(f"{human.name}загинув...")
        break