import os


def find_symbol_links(start_path):
    code = ''
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.islink(fp):
                code += "['{}', '{}'],\n".format(os.path.relpath(os.path.realpath(fp)), os.path.relpath(fp))
    with open('symlink_list.txt', 'w') as f:
        f.write(code)


find_symbol_links('.')
