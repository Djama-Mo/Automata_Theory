import re
import sys


def main():

    directory = '/home/djama/Рабочий стол'
    pattern = re.compile(r'((^[a-zA-Z])([a-zA-Z\d]{0,15})\[\]=\{(\-*\d+\,*)+\})|((^[a-zA-Z])([a-zA-Z\d]{0,15})\[\d{1,9}\]=\{(\-*\d*\,*)+\})', re.MULTILINE)

    tmp_result = get_from_file(directory, pattern)

    if len(sys.argv) > 1:
        show_in_console(tmp_result)
    else:
        put_in_file(directory, tmp_result)
        print("Result have been successfully written into specified text file")


def get_from_file(location, pattern):

    with open(location + '/templates.txt', 'r') as fh:
        strings = fh.read()
    return re.finditer(pattern, strings)

def put_in_file(location, result):

    with open(location + '/result.txt', '+a') as fh:
        for string in result:
            finish_string = modify_string(string.group())
            fh.write(f'{finish_string}\n')
    return 0

def show_in_console(result):

    for string in result:
        finish_string = modify_string(string.group())
        print(f'{finish_string}')

    return 0

def modify_string(string):

    finish_string = str(string)

    length = len(finish_string)
    first = finish_string.find('[')
    second = finish_string.find(']')
    count = second - first
    if count == 1:
        index = finish_string.find('{')
        mount = 0
        while index != length:
            if finish_string[index] == ',':
                mount += 1
            index += 1
        mount += 1
    else:
        mount = int(finish_string[first + 1: second])

    finish_string = finish_string[0:first] + '-' + f'{mount}'

    return finish_string


if __name__ == '__main__':
    main()