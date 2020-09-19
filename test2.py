import os
# import random as r
from random import randint, shuffle
import libs

print(os.getcwd())
# print(r.randint(1, 100))
print(randint(13, 100))
l = [1, 2, 3, 4, 5]
shuffle(l)
print(l)

print(libs.get_count('adabracadabra', 'a'))
print(libs.get_len('adabracadabra'))

print(__name__)