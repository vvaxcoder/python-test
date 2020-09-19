x = 75
user_num = 0
cnt = 0

while True:
    user_num = int(input('I wish a number from 1 to 100 - try to resolve it: '))
    cnt += 1
    if user_num == x:
        print(f'You are win the number for {cnt} times.')
        print('Thanks for game.')
        break
    elif user_num > x:
        print('My number is less than yours')
    else:
        print('My number is grater than yours')
