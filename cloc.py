import os
import sys
import time


def check_file_extension(file_path, file_extensions):

    result = False
    for file_ext in file_extensions:
        if file_path.endswith(file_ext):
            result = True
    return result


def cloc(file_extensions):

    start_time = time.time()
    sys.stdout.write('\nstarting cloc script for extension ' +
                     str(file_extensions) + '\n')

    if sys.argv.__len__() < 2:
        sys.stderr.write('\ninsufficient arguments\n\n')
        exit(-1)

    folder_path = sys.argv[1]
    sys.stdout.write('folder path: ' + os.path.abspath(folder_path) + '\n')

    if not os.path.isdir(folder_path):
        sys.stderr.write('\ninvalid directory:\n' + folder_path + '\n')
        exit(-1)

    total_line_count = 0
    for root, sub_folders, files in os.walk(folder_path):
        for file in files:
            matches = check_file_extension(file, file_extensions)
            if matches:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as fp:
                    for count, line in enumerate(fp):
                        pass
                total_line_count += count + 1

    sys.stdout.write('\ntotal line count: ')
    sys.stdout.write(str(total_line_count))
    sys.stdout.write('\n')

    exec_time = str(round(time.time() - start_time, 2))
    sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n\n')
