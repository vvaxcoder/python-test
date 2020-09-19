import os

# tree = os.walk('folder')
# for files in tree:
#     print(files)

def read_dir(folder):
    #raspakovka kortezha
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        sub_indent = ' ' * 4 * (level + 1)
        print(f'{indent}[{os.path.basename(root)}]')
        # print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent}{file}')

read_dir('folder')