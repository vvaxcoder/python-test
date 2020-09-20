# Classes with constructor

from classes import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Kate')
# person2.__age = 31 # not set, because this property is a pseudo-private 

# print(person2._Person__age)

# person2.set_age(31)
# print(person2.age)

person2.age = 31
person2.print_info()