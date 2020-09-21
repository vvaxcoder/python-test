# Decorators

# def test_dec():
#     return 'Test decorators'

# def super_func(func):
#     print('Test super function')
#     print(test_dec())

# super_func(test_dec)

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper

# @my_decorator
# def func_test():
#     print('Function func_test is called')

# # test = my_decorator(func_test)
# # test()

# func_test()

def make_title(fn):
    def wrapper():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapper

@make_title
def decorator_examle():
    return 'from, decorator'

print(decorator_examle())