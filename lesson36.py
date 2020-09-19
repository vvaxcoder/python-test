#Classes and OOP

class A:
    property1 = 'Property1'
    property2 = 'Property2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name

a = A()
b = A()

# print(a)
print(a.property1)
print(a.say_hi())
print(b.say_hi('John'))