import zipfile
import os


def compress_to_multi_zip(arch_name, start_path, zip_max_size):
    total_size = 0
    notify_size = 0
    total_size_all = 0
    n = 1
    zip_file = zipfile.ZipFile("{}_{}.zip".format(arch_name, n), 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                if total_size + os.path.getsize(fp) > zip_max_size:
                    zip_file.close()
                    total_size = 0
                    n += 1
                    zip_file = zipfile.ZipFile("{}_{}.zip".format(arch_name, n), 'w', zipfile.ZIP_DEFLATED)
                zip_file.write(fp, fp)
                fsize = os.path.getsize(fp)
                total_size += fsize
                notify_size += fsize
                total_size_all += fsize
                if notify_size > 100 * 1024 * 1024:
                    notify_size = 0
                    print(total_size_all)
                  
    zip_file.close()


compress_to_multi_zip('all_src', 'src', 1024 * 1024 * 1024)
