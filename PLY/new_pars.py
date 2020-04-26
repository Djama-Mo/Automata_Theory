import LexClass
import ply.yacc as yacc
import time


def main():
    print("Main's starting")
    parser = Parser()
    file_from = open('templates.txt', 'r')
    # tmp = file_from.read()
    start = time.time()
    for line in file_from:
        parser.CheckString(line.rstrip())
    # parser.CheckString(tmp)
    end = time.time()
    with open('PLY_time.txt', 'a') as time_file:
        time_file.write(str('{:f}'.format(end - start)) + '\n')
    parser.put_in_file()
    file_from.close()
    parser.file.close()
    print('time : ' + str(end - start))
    print('\n')
    # print(parser.a)
    print("Main's ending")


class Parser:
    tokens = LexClass.Lexer.tokens

    def __init__(self):
        self._lexer = LexClass.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._a = dict()
        self.file = open('Parser_Results.txt', 'a+')
        self.flag = False

    def CheckString(self, string):
        # self._a.clear()
        self.flag = False
        result = self._parser.parse(string)
        return result

    # def p_address_list(self, p):
    #     """address_list : address
    #                     | address_list address"""

    def p_address(self, p):
        """address : NAME SIZE ELEMENTS
                    | NAME SIZE_ZERO ELEMMH FIG_BR"""
        if len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
        elif len(p) == 5:
            p[0] = p[1] + p[2] + p[3] + p[4]
        self.flag = True
        if self._a.get(p[1]) is None:
            self._a[p[1]] = 1
        else:
            self._a[p[1]] += 1

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]

    # def p_err_list_zero_type(self, p):
    #     """err_list : """
    #
    # def p_err_list_first_type(self, p):
    #     """err_list : err"""
    #     p[0] = p[1]
    #
    # def p_err_list_second_type(self, p):
    #     """err_list : err_list err"""
    #     p[0] = p[1] + p[2]


    def p_error(self, p):
        print('Unexpected token', p)

    def p_address_zero_err_type(self, p):
        """address : err NL"""
        p[0] = p[1] + p[2]

    def p_address_first_err_type(self, p):
        """address : NAME err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_address_second_err_type(self, p):
        """address : NAME SIZE err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_address_third_err_type(self, p):
        """address : NAME SIZE ELEMENTS err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_address_fourth_err_type(self, p):
        """address : NAME SIZE_ZERO err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_address_fifth_err_type(self, p):
        """address : NAME SIZE_ZERO ELEMMH err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_address_sixth_err_type(self, p):
        """address : NAME SIZE_ZERO ELEMMH FIG_BR err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def put_in_file(self):
        for key in self._a.keys():
            self.file.write(key + ' - ' + str(self._a[key]) + '\n')

    def a(self):
        return self._a


if __name__ == '__main__':
    main()
