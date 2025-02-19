import random
import time
from time import sleep


class Human:
    def __init__(self, name):
        self.name = name
        self.money = random.randint(5,30)
        self.happiness = random.randint(10,100)
        self.satiety = random.randint(5,100)
        self.stamina = 100
        self.alive = True
        self.work_today = False
        self.weekday = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        self.current_day_index = 0
        self.current_day = self.weekday[self.current_day_index]
        self.job = "Нема"
        self.car = "Нема"
        self.house = "Є"

    def get_job(self):
        if self.stamina >= 60:
            self.satiety -= 10
            self.happiness -= 5
            self.work_today = True
            random_job = random.randint(1, 5)
            if random_job == 1:
                random_job = random.randint(1, 3)
                if random_job == 1:
                    job = Job("Прибиральник", 20, 10, 80)
                elif random_job == 2:
                    job = Job("Офісний працівник", 30, 5, 60)
                elif random_job == 3:
                    job = Job("Шеф", 50, 3, 40)
                self.job = job
                print(f"{self.name}отримав роботу: {job.position}")
            else:
                print(f"{self.name}не знайшов роботу. Щастя {human.happiness}, Ситість: {human.satiety}")
            self.stamina -= 60
            human.simulate_day()
        else:
            print(f"{self.name}дуже втомився щоб шукати роботу. Стаміна: {self.stamina}")
            human.simulate_day()

    def buy_food(self):
        if self.stamina >= 10:
            products = random.randint(1, 5)
            price = random.randint(2, 5)
            price *= products

            if self.money >= price:
                house.food += products
                self.money -= price
                print(f"{self.name}купив їжу. Їжі вдома: {house.food}.")
                self.stamina -= 10
                human.simulate_day()
            else:
                print(f"{self.name}не вистачає грошей на їжу!")
                self.happiness -= random.randint(5, 10)
        else:
            print(f"{self.name}сильно втомився щоб купити їжі. Стаміна: {self.stamina}")
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
        if self.stamina >= 60:
            self.satiety -= 10
            self.money += self.job.salary
            self.happiness -= self.job.happiness_loss
            self.stamina -= self.job.stamina_loss
            self.work_today = True
            print(f"{self.name}працював і заробив {self.job.salary}. Баланс: {self.money}, Ситість: {self.satiety}, Щастя: {self.happiness}")
        else:
            print(f"{self.name}дуже втомився щоб працювати. Стаміна: {self.stamina}")
        human.simulate_day()

    def have_fun(self):
        if self.stamina >= 20:
            print(f"1.Пограти в доту, 2.Полежати на дивані, 3.Відправиться в подорож на машині, 4.Назад. Щастя: {self.happiness}")
            match input("Як відпочити: "):
                case "1":
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
                case "2":
                    print(f"{self.name}захотів полежати на дивані")
                    self.happiness += 10
                    print(f"{self.name}відпочиває. Щастя: {self.happiness}")
                case "3":
                    if self.car != "Нема" and self.car.fuel >= self.car.fuel_consumption:
                        print("1.На рибалку, 2.У казино")
                        match input("Куди вирушити?: "):
                            case "1":
                                print(f"{self.name}вирушив на рибалку")
                                self.car.fuel -= self.car.fuel_consumption
                                self.car.durability -= random.randint(5, 10)
                                if random.randint(1, 2) == 1:
                                    caught_fish = random.randint(1, 10)
                                    house.food += caught_fish
                                    self.happiness += 20
                                    print(f"{self.name}зловив {caught_fish} риб. Їжі вдома: {house.food}, Щастя: {self.happiness}, Паливо: {self.car.fuel}, Міцність машини: {self.car.fuel}")
                                else:
                                    self.happiness += 10
                                    print(f"{self.name}не зловив рибу. Щастя: {self.happiness}, Паливо: {self.car.fuel}, Міцність машини: {self.car.fuel}")
                            case "2":
                                while True:
                                    print(f"\nГроші: {human.money}")
                                    self.bit = 0
                                    if self.bit > self.money or self.money <= 0:
                                        print("Не вистачає грошей")
                                        print("Поставити машину? 1.Так, 2.Ні")
                                        match input("Згодні? "):
                                            case "1":
                                                if self.car == "Нема":
                                                    print("Немає машини")
                                                    human.simulate_day()
                                                else:
                                                    self.bit_car = True
                                            case "2":
                                                self.stamina = 0
                                                self.happiness -= 10
                                                self.bit = self.car.price
                                                print(
                                                    f"{self.name}повернувся додому. Щастя: {self.happiness}, Паливо: {self.car.fuel}, Міцність машини: {self.car.fuel}")
                                                human.simulate_day()
                                    else:
                                        self.bit = int(input("Скільки грошей поставити? "))
                                        self.bit -= self.money

                                    print("1.Пряма ставка, 2.Ставка на колір 3.Закінчити грати")
                                    match input("Що вибрати: "):
                                        case "1":
                                            bid_on = input("На яке число поставити? ")

                                            numerical_roulette = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                                  17,
                                                                  18, 19, 20, 21,
                                                                  22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                                                                  35,
                                                                  36, 37]
                                            random_scroll = random.randint(10, 50)
                                            subtraction = 0
                                            for i in range(0, random_scroll):
                                                if subtraction == len(numerical_roulette) - 1:
                                                    subtraction = 0
                                                else:
                                                    subtraction += 1
                                                print(f"\rЕлементи: {numerical_roulette[subtraction]}", end=" ")

                                                time.sleep(0.1)
                                            if bid_on == numerical_roulette[subtraction]:
                                                self.money = self.bit * 8
                                                print(f"\n {self.name}переміг. Гроші: {human.money}")
                                            else:
                                                if self.bit_car:
                                                    self.car = "Нема"
                                                    self.happiness = 0
                                                    self.bit_car = False
                                                    print(f"\n{self.name}програв машину. Щастя: {self.happiness}")
                                                else:
                                                    self.bit_car = False
                                                    print(f"\n{self.name}програв. Гроші: {human.money}")
                                        case "2":
                                            selected_color = "Не обраний"
                                            print("1.Червоний, 2. Чорний")
                                            match input("На який колір ставити?: "):
                                                case "1":
                                                    selected_color = "Червоний"
                                                case "2":
                                                    selected_color = "Чорний"
                                            color_roulette = ["Червоний", "Чорний"]
                                            random_scroll = random.randint(10, 50)
                                            subtraction = 0
                                            for i in range(0, random_scroll):
                                                if subtraction == len(color_roulette) - 1:
                                                    subtraction = 0
                                                else:
                                                    subtraction += 1
                                                print(f"\rЕлементи: {color_roulette[subtraction]}", end=" ")

                                                time.sleep(0.1)
                                            if selected_color == color_roulette[subtraction]:
                                                self.money = self.bit * 2
                                                print(f"\n{self.name}переміг. Гроші: {human.money}")
                                            else:
                                                if self.bit_car:
                                                    self.car = "Нема"
                                                    self.happiness = 0
                                                    self.bit_car = False
                                                    print(f"\n{self.name}програв машину. Щастя: {self.happiness}")
                                                else:
                                                    self.bit_car = False
                                                    print(f"\n{self.name}програв. Гроші: {human.money}")
                                        case "3":
                                            self.money += self.bit
                                            self.bit_car = False
                                            print(f"\n{self.name}закінчив грати. Гроші: {human.money}")
                                            break
                        self.stamina = 0
                    else:
                        if self.car == "Нема":
                            print(f"{self.name}немає машини")
                        else:
                            print(f"Не може вирушити в подорож. Паливо: {self.car.fuel}")
                case "4":
                    human.simulate_day()
                case _:
                    print("Некоректне значення")
                    self.have_fun()
        else:
            print(f"{self.name}дуже втомився для ігор. Стаміна: {self.stamina}")
        self.stamina -= 20
        human.simulate_day()

    def clean_house(self):
        if self.stamina >= 80:
            if self.house:
                self.house.mess = 0
                self.happiness += 10
                self.stamina -= 80
                print(f"{self.name} прибрав у домі. Щастя: {self.happiness}, Стаміна: {self.stamina}")
                human.simulate_day()
        else:
            print(f"{self.name}дуже втомився для прибирання. Стаміна: {self.stamina}")
            human.simulate_day()

    def buy_car(self):
        print("1. Nissan, ціна: 100, витрата палива: 60")
        print("2. BMW, ціна: 120, витрата палива: 40")
        print("3. Toyota, ціна: 240, витрата палива: 10")
        match input("Яку купити?: "):
            case "1":
                if self.money >= 100:
                    self.car = Auto("Nissan", 100, 100, 40, 100)
                    self.money -= self.car.price
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case "2":
                if self.money >= 120:
                    self.car = Auto("BMW", 100, 100, 30, 120)
                    self.money -= self.car.price
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case "3":
                if self.money >= 240:
                    self.car = Auto("Toyota", 100, 100, 20, 240)
                    self.money -= self.car.price
                    print(f"Купив {self.car.brand}")
                else:
                    print("Немає грошей на машину")
            case _:
                print("Некоректне значення")
        self.happiness += 10
        human.simulate_day()

    def check_status(self):
        self.house.mess += random.randint(5, 10)
        print("Події дня:")
        if self.happiness <= 0:
            self.alive = False
        else:
            if self.satiety < 10:
                print(f"{self.name}зголоднів")
                self.happiness -= random.randint(10, 20)
            elif self.job == "Нема":
                print(f"{self.name}безробітний")
                self.happiness -= 3
            elif self.current_day not in ["Субота", "Неділя"] and not self.work_today:
                print(f"{self.name}потрібно сходити на роботу")
                self.happiness -= 3
            elif self.current_day in ["Субота", "Неділя"]:
                print("Cьогодні вихідні можна відпочити")
                self.happiness += 5
            elif house.mess > 60:
                self.happiness -= 10
                print("У будинку брудно. Може варто прибрати?")

    def end_day(self):
        if self.job != "Нема" and not self.work_today and self.current_day not in ["Субота", "Неділя"]:
            Job.omissions += 1
        if Job.omissions == 4 :
            print(f"{self.name}загубив роботу")
            Job.omissions == 0
            self.job = "Нема"
        if self.happiness <= 0:
            self.alive = False

    def simulate_day(self):
        if self.stamina > 0:
            print(f"\nСтаміна: {self.stamina}")
            match input("Що робити?: "):
                case "1":
                    if human.job == "Нема" and not self.work_today:
                        self.get_job()
                    else:
                        if self.current_day not in ["Субота", "Неділя"] and not self.work_today:
                            self.work()
                        else:
                            print("Ви не можете працювати сьогодні")
                            human.simulate_day()
                case "2":
                    print(f"Купити: 1.Їжу, 2.Машину, 3.Назад. Гроші: {human.money}")
                    match input("Що купити?: "):
                        case "1":
                            self.buy_food()
                        case "2":
                            self.buy_car()
                        case "3":
                            human.simulate_day()
                        case _:
                            print("Некоректне значення")
                            human.simulate_day()
                case "3":
                    self.eat()
                case "4":
                    self.clean_house()
                case "5":
                    self.have_fun()
                case "6":
                    self.satiety -= 5
                    self.happiness += 5
                    self.end_day()
                    print(f"{self.name}Заснув")
                case _:
                    print("Некоректне значення")
                    human.simulate_day()
        else:
            self.end_day()
            print(f"{self.name}Устал")

class House:
    def __init__(self):
        self.mess = 0
        self.food = random.randint(1,5)

class Job:
    omissions = 0
    def __init__(self, position, salary, happiness_loss, stamina_loss):
        self.position = position
        self.salary = salary
        self.happiness_loss = happiness_loss
        self.stamina_loss = stamina_loss


class Auto:
    def __init__(self, brand, fuel, durability, fuel_consumption, price):
        self.brand = brand
        self.fuel = fuel
        self.durability = durability
        self.fuel_consumption = fuel_consumption
        self.price = price

inp_name = input("Ведіть ім'я персонажа: ")
human = Human(inp_name + " ")
house = House()
human.house = house

print("\nСтатистика:\n")
print(f"Ім'я: {human.name}")
print(f"Гроші: {human.money}")
print(f"Щастя: {human.happiness}")
print(f"Ситість: {human.satiety}")
print(f"Забруднення у квартирі: {house.mess}")
print(f"Їжі у квартирі: {house.food}")

for day in range(1, 100):
    if human.alive:
        human.work_today = False
        human.stamina = 100

        print(f"\nДень: {day}")
        print(f"Сьогодні: {human.current_day}")
        print(f"\nГроші: {human.money}, Щастя {human.happiness}, Ситість: {human.satiety}, Забруднення у квартирі: {house.mess}\n")

        if human.job == "Нема":
            print("1. Шукати роботу")
        else:
            print("1. Працювати")
        print("2. Купити")
        print("3. Їсти")
        print("4. Прибрати в будинку")
        print("5. Відпочивати")
        print("6. Спать\n")

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
        print(f"\n{human.name}загинув...")
        sleep(10000)
        break

print("\nСтатистика:\n")
if human.alive:
    print(f"{human.name}Вижив! {day} днів!")
else:
    print(f"{human.name}Протримався: {day}")
print(f"Гроші: {human.money}")
print(f"Щастя: {human.happiness}")
print(f"Ситість: {human.satiety}")
print(f"Забруднення у квартирі: {house.mess}")
print(f"Їжі у квартирі: {house.food}")
if human.job != "Нема":
    print(f"Робота: {human.job.position}")
else:
    print(f"Робота: Нема")
print(f"Кількість пропусків роботи: {Job.omissions}")
if human.car != "Нема":
    print(f"Машина: {human.car.brand}")
else:
    print(f"Машина: Нема")
sleep(10000)