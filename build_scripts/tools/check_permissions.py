import os
import stat


def find_symbol_links(start_path):
    code = ''
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                if 0 != os.stat(fp)[stat.ST_MODE] & (stat.S_IXOTH | stat.S_IXGRP | stat.S_IXUSR):
                    code += "'{}',\n".format(os.path.relpath(fp))
    with open('exec_files_list.txt', 'w') as f:
        f.write(code)


find_symbol_links('.')
