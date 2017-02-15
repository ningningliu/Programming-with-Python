from person import Person

class Manager(Person):
    # Inherited from class Person
    def giveRaise(self, percent, bonus=0.1):
        #self.pay *= (1.0 + percent + bonus)
        # Alternative method
        Person.giveRaise(self,percent + bonus)

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age=52, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(0.2)
    print(tom.pay)




# bob = Person (name = 'Bob Smith', age =42, pay = 10000)
# sue = Person (name = 'Sue Jones', age =45, pay = 20000)
# tom = Manager(name = 'Tome Doe', age = 50, pay = 30000)
# db = [bob, sue, tom]
#
# for obj in db:
#     obj.giveRaise(0.1)       # Polymorphism : customise giveRaise for class Manager
# for obj in db:
#     print(obj.lastName(), '=====>', obj.pay)


