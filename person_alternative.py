"""
Refactoring the code
"""

class Person:
    """
    a general person : data  logic
    """
    def __init__(self, name, age,pay =0, job= None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRise(self, percent):
        self.pay *= (1.0 +percent)

    def __str__(self):
        return ('< %s => %s ; %s , %s>' %(self.__class__.__name__, self.name, self.job, self.pay))


class Manager(Person):
    """
    a person with custom raise inherits general lastname, str
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age,pay,'manager')

    def giveRise(self, percent, bonus = 0.1):
        Person.giveRise(self, percent+bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith',44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager('Tom Doe',age= 50, pay = 50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRise(.10)
        print(obj)  # run common __str__
