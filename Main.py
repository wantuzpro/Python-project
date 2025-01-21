class Human:
    height = 170
    age = 21

class Student(Human):
    height = 180
    age = 17

class Worker(Human):
    pass

Nick = Student()
Lion = Worker()

print(Nick.height)
print(Lion.height)
print(Nick.age)
print(Lion.age)
