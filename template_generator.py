import xeger
import random
import numpy
import sys

def main():

    count_of_templates = 0
    if len(sys.argv) > 1:
        count_of_templates = int(sys.argv[1])
    else:
        choice = Menu()
        tmp_choice = choice.choice()

        if tmp_choice == 2:
            tmp_count = choice.call_generator()
            if tmp_count == 0:
                count_of_templates = random.randint(10, 100)
            else:
                count_of_templates = tmp_count
        elif tmp_choice == 1:
            choice.default_input()

    directory = '/home/djama/Рабочий стол/'
    bool_choice = (True, False)

    if count_of_templates:
        for _ in range(count_of_templates):
            valid = random.choice(bool_choice)
            make_square_par_empty = random.choice(bool_choice)
            make_square_fig_empty = random.choice(bool_choice)
            template = Template(valid, make_square_par_empty, make_square_fig_empty)
            put_in_file(directory, template.result)

        print('Templates have been successfully written into specified text file')

class Template(object):

    __min_arr_cnt, __max_arr_cnt, __max_name_length, __max_cnt_length, __min_int_val, __max_int_val, __critical_arr_length, instances_amount = 1, 11, 15, 9, -32768, 32767, 100, 0

    '''Main constructor'''
    def __init__(self, valid=True, make_square_par_empty=False, make_square_fig_empty=False):
        self.make_square_par_empty = make_square_par_empty
        self.make_square_fig_empty = make_square_fig_empty
        if make_square_fig_empty and make_square_par_empty:
            valid = False
        self.valid = valid

        self.arr_name = self.__arr_name_generator(self.valid)
        self.arr_cnt = self.__arr_cnt_generator(self.make_square_par_empty)
        self.arr = self.__arr_generator(self.make_square_fig_empty)
        self.result = f'{self.arr_name}[{self.arr_cnt}]={{{self.arr}}}'

    '''Overriding repr method'''
    def __repr__(self):
        if self.valid:
            description = 'good template..'
        else:
            description = 'bad template..'
        return description

    '''Overriding str method'''
    def __str__(self):
        # TODO: add more functionality
        return self.result

    def __arr_name_generator(self, valid=True):
        x = xeger.Xeger(15)

        if valid:
            ptr_name = x.xeger(r'[a-zA-Z]([a-zA-Z\d]*)')
        else:
            ptr_name = x.xeger(r'[0-9]([a-zA-Z\d]*)')

        return ptr_name

    def __arr_cnt_generator(self, make_square_par_empty=False):
        if make_square_par_empty:
            result = ''
        else:
            x = xeger.Xeger(self.__max_cnt_length)
            result = x.xeger(r'\d*')

            try:
                result = '' if result[0] == '0' else result
            except IndexError as err:
                pass

        return result

    def __arr_generator(self, make_square_fig_empty=False):
        if make_square_fig_empty:
            res = ''
        else:
            if not all([self.arr_cnt, self.arr_cnt is not '0']):
                res = ','.join(str(random.randint(self.__min_int_val, self.__max_int_val)) for _ in
                               range(random.randint(self.__min_arr_cnt, self.__max_arr_cnt)))
            else:
                res = ','.join(str(random.randint(self.__min_int_val, self.__max_int_val)) for _ in range(
                    random.randint(0, self.__max_arr_cnt if int(self.arr_cnt) > self.__critical_arr_length else int(
                        self.arr_cnt))))

        return res


def put_in_file(location, content):
    with open(location + '/templates.txt', 'a+') as fh:
        fh.write(f'{content}\n')
    return 0


class Menu(object):

    def default_input(self):

        print('Enter 0 if u wanna to finish\n')
        while True:
            string = str(input())
            if string == '0':
                break
            else:
                put_in_file('/home/djama/Рабочий стол/', string)
        return -1

    def call_generator(self):

        num = 0
        while True:
            choice = int(input("Choose:\n1 - generate automatically\n2 - input the count\n--> "))
            if choice == 2:
                num = int(input("Enter the count of strings to generate its\n--> "))
                break
            elif choice == 1:
                break
            else:
                print('Incorrect input, pls try again\n')
        return num

    def choice(self):

        flag = 0
        while True:
            choice = int(input("Choose:\n1 - input the strings\n2 - call the generator\n--> "))
            if choice == 2:
                flag = 2
                break
            elif choice == 1:
                flag = 1
                break
            else:
                print('Incorrect input, pls try again\n')
        return flag

if __name__ == '__main__':
    main()