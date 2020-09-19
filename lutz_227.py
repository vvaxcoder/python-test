import sys


def test():
    while True:
        reply = input('Enter text:')
        if reply == 'stop':
            return
        try:
            num = int(reply)
        except:
            print('Bad!' * 6)
        else:
            print(int(reply) ** 2)
    print('Bye')


test()
