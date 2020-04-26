import re
import sys
import time


def main():
    directory = '/home/djama/Рабочий стол'
    pattern = re.compile(r'((^[a-zA-Z])([a-zA-Z\d]{0,15})\[0?\]=\{(\-*\d+\,*)+\})|((^[a-zA-Z])([a-zA-Z\d]{0,15})\[\d{1,9}\]=\{(\-*\d*\,*)*\})',re.MULTILINE)

    start = time.time()
    tmp_result = get_from_file(directory, pattern)
    end = time.time()

    with open('RegEx_time.txt', '+a') as time_file:
        time_file.write(f"{'{:f}'.format(end - start)}\n")

    if len(sys.argv) > 1:
        show_in_console(tmp_result)
        print(end - start)
    else:
        put_in_file(directory, tmp_result)
        print(end - start)
        print("Result have been successfully written into specified text file")


def get_from_file(location, pattern):
    with open(location + '/templates.txt', 'r') as fh:
        strings = fh.read()
    return re.finditer(pattern, strings)


def put_in_file(location, result):
    with open(location + '/result.txt', '+a') as fh:
        for string in result:
            finish_string = modify_string(string.group())
            if finish_string:
                fh.write(f'{finish_string}\n')
    return 0


def show_in_console(result):
    for string in result:
        finish_string = modify_string(string.group())
        if finish_string:
            print(f'{finish_string}')

    return 0


def modify_string(string):
    finish_string = str(string)

    length = len(finish_string)
    first = finish_string.find('[')
    second = finish_string.find(']')
    count = second - first

    index = second + 2
    mount_by_commas = 0
    while index != length:
        if finish_string[index] == ',':
            mount_by_commas += 1
        index += 1
    if mount_by_commas:
        mount_by_commas += 1

    try:
        simple_count = int(finish_string[first + 1: second])
    except ValueError:
        simple_count = 0

    if count == 1 or finish_string[first + 1] == '0':
        mount = mount_by_commas
    else:
        mount = simple_count

    finish_string = finish_string[0:first] + '-' + f'{mount}'

    if mount_by_commas != 0 and simple_count != 0 and mount_by_commas > simple_count:
        finish_string = ''

    return finish_string


if __name__ == '__main__':
    main()
