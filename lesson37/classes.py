# Full incapsulation in Python is not provided
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        # self._age = 25 # it's like a protected, but by agreement
        self.__age = age  # it's like a private, but by agreement

    def print_info(self):
        print(f'Congratulation, {self.name} with age: {self.__age}')

    # def get_age(self):
    #     return self.__age

    # def set_age(self, value):
    #     if value in range(0, 101):
    #         self.__age = value

    # example of decorator that equal a getter
    @property
    def age(self):
        return self.__age

    # example of decorator that equal setter
    @age.setter
    def age(self, value):
        if value in range(0, 101):
            self.__age = value

class Employee(Person): # example of inheritance
    def __init__(self, name, age, company):
        super().__init__(name, age) # example of polymorphism
        self.company = company

    def more_info(self):
        print(f'Name: {self.name} works in {self.company}')

    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')

    def __str__(self):
        # return f'Name: {self.name}'
        return 'Class ' + self.__class__.__name__