#number_1 and 2
class Parent:
    def __init__(self, rost, ves, age):
        self.rost = rost
        self.ves = ves
        self.age = age
    def say_one(self):
        print(F"Iam {self.age} years old")
        print(F"I'm hanging {self.ves}")
        print(F"my height {self.rost}")
    def activity(self, work):
        self.work = work
        return F'{self.work}'
    def can(self, may):
        self.may = may
        return F'{self.may}'
#number_3
class Child(Parent):
    def kid(self, young):
        self.young = young
        return F'{self.young}'

    def baby(self, scream):
        self.scream = scream
        return F'{self.scream}'
#number_4
    def make(self):
        self.rost += 0.20
        self.ves += 5
        self.age += 1
#number_5
    def made(self):
        if self.age >= 5:
         print('Старею я.....')
m = Child(1.50,50,10)
m.make()
c = Child(1.50,50,10)
c.say_one()
print(c.kid("Я еще молод, не могу работать "))
print(c.baby('Я умею только кричать'))
m2 = Child(1.50,50,10)
m2.made()
d = Parent(1.90, 90, 40)
d.say_one()
print(d.activity("Зарабатывать деньги "))
print(d.can('Я умею много чего '))