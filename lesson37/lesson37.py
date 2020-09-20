# Classes with constructor

from classes import Person, Employee

person1 = Person('John', 29)
person1.print_info()

person2 = Person('Kate', 31)
# person2.__age = 31 # not set, because this property is a pseudo-private 

# print(person2._Person__age)

# person2.set_age(31)
# print(person2.age)

person2.age = 31
person2.print_info()

employee = Employee('Nick', 33, 'Roga_and_Kopyta')
employee.print_info()
employee.more_info()
print(employee)