class Grandparent:
    height = 180
    age = 80

class Parent(Grandparent):
    height = 180
    age = 40

class Child(Parent):
    age = 18

Ann = Child()
print(Ann.height)