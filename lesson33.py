# f = open('file.txt', 'r', encoding='utf-8')
f = open('file.txt', 'a', encoding='utf-8')
# text = f.read(2)
# print(f.encoding)

lines = ['Another new line had added', 'Another new line had added']
# f.write('New line had added\n')
# for line in lines:
#     f.write(line + '\n')
f.writelines(lines + '\n')

f.close()
