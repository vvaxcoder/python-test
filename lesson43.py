# Lambda

# def get_square(num):
#     return num ** 2

# print(get_square(13))

get_square = lambda num: num ** 2 # this is old school :)
print(get_square(11))

# OR with new Python standard
print((lambda num: num ** 2)(11))