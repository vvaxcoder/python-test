def odd_ball(arr):
    return arr.index("odd") in arr

print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"])) # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"])) # False
print(odd_ball(["even", 10, "odd", 2, "even"])) # True

"""
2
"""
def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

def find_sum2(n):
    return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)

print(find_sum(5)) # return 8 (3 + 5)
print(find_sum(10)) # return 33 (3 + 5 + 6 + 9 + 10)

print(find_sum2(5)) # return 8 (3 + 5)
print(find_sum2(10)) # return 33 (3 + 5 + 6 + 9 + 10)

"""
3
"""
names = ["Rayn", "Kieran", "Mark", "John", "David", "Paul"]

def get_names(names):
    return [x for x in names if len(x) == 4]

print(get_names(names))