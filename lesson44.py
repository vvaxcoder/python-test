# Regular Expressions

import re

# s = 'This is a test string. And this one is another string.'
# pattern = 'string'

# print(s.find(pattern))
# print(pattern in s)

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No matched')

# match = re.search(pattern, s)
# print(match)
# print(match.start())
# print(match.end())

# print(re.match(pattern, s))

# print(re.findall(pattern, s))

# print(re.split(r'\.', s, 1))

s = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
А это строка с разными символами: "!", "@", "-", "?", "__"
a\\b\\tc
test string'''

# pattern = r'\w+'
# pattern = r'[а-яА-ЯёЁ]+'
# pattern = r'[0-9]+'
# pattern = r'a\\b\\tc'
# pattern = r'^\w+$'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

def validate_email(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)

print(validate_email('mail@mail.com'))
print(validate_email('ivanov@bank'))
print(validate_email('mail@google.com.ua'))