class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Subodh", 14)
del person1.age
print(person1.name)
print(person1.age)
