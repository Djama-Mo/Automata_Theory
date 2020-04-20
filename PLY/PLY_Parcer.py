import LexClass
import ply.yacc as yacc


def main():
    print("Main's starting")
    parser = Parser()
    print(parser.CheckString('Array[]={}'))
    print('\n')
    print(parser.a)
    print("Main's ending")


class Parser:
    tokens = LexClass.Lexer.tokens

    def __init__(self):
        self._lexer = LexClass.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._a = dict()
        self.file = open('Parser_Result.txt', 'a+')
        self.flag = False

    def CheckString(self, string):
        self.flag = False
        result = self._parser.parse(string)
        return result

    def p_address(self, p):
        """address : ALPHA NAME SIZE ELEMENTS |
                    ALPHA NAME SIZE_ZERO ELEMMH"""
        if p[3] == 'SIZE':
            p[0] = p[1] + p[2] + p[3] + p[4]
        elif p[3] == 'SIZE_ZERO':
            p[0] = p[1] + p[2] + p[3] + p[4]
        self.flag = True
        if self._a.get(p[1]) is None:
            self._a[p[1]] = 1
        else:
            self._a[p[1]] += 1

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]

    def p_error(self, p):
        print('Unexpected token', p)

    def p_address_zero_err_type(self, p):
        """address : err NL"""
        p[0] = p[1] + p[2]

    def p_address_first_err_type(self, p):
        """address : ALPHA err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_address_second_err_type(self, p):
        """address : ALPHA NAME err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_address_third_err_type(self, p):
        """address : ALPHA NAME SIZE err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_address_fourth_err_type(self, p):
        """address : ALPHA NAME SIZE ELEMENTS err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_address_fifth_err_type(self, p):
        """address : ALPHA NAME SIZE_ZERO err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_address_sixth_err_type(self, p):
        """address : ALPHA NAME SIZE_ZERO ELEMMH err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def put_in_file(self):
        for key in self._a.keys():
            self.file.write(key + str(self._a[key]) + '\n')

    def a(self):
        return self._a

if __name__ == '__main__':
    main()
