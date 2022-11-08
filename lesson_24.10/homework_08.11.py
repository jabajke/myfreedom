class Parent:
    def __init__(self, age, weight, growth):
        self.age = age
        self.weight = weight
        self.growth = growth
    def main_activity(self):
        print('Зарабатывать деньги')
    def skills(self):
        print('Я умею много чего')
sasha = Parent(40, 80, 180)
print(sasha.age)
print(sasha.weight)
print(sasha.growth)
print(sasha.main_activity())
print(sasha.skills())


class Child:
    def __init__(self, age1, weight1, growth1):
        self.age1 = age1
        self.weight1 = weight1
        self.growth1 = growth1
    def main_activity1(self):
        print('Я еще молод, не могу работать')
    def skills1(self):
        print('Я умею только кричать')
    def rastet_maloy(self, age1, weight1, growth1):
        print(age1 + 1, weight1 + 5, growth1 + 20)

maloy = Child(age1= 1, weight1= 5, growth1= 70)
print(maloy.age1)
print(maloy.weight1)
print(maloy.growth1)
print(maloy.main_activity1())
print(maloy.skills1())
print(maloy.rastet_maloy())




