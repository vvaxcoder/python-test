# Exceptions

# print('Berofe try-except')

# try:
#     num = 100 / 0
# except ZeroDivisionError:
#     num = 0
# else: #optional
#     print('Else')
# finally: #optional
#     print('Finally')

# print(num)
# print('After try-except')

while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('Number must be grather than zero')
    except ValueError:
        print('Type must be a number')