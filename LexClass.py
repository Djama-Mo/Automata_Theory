import ply.lex as lex
import time


def main():
    print("Main's starting")
    file = open('templates.txt', 'r')
    tmp = file.read()
    file.close()

    start = time.time()
    lexer = Lexer()
    lexer.input(tmp)
    while True:
        token = lexer.token()
        if token is None:
            break
        print(token)
        # if token.type != 'UNKNOWN' and token.type != 'NL':
        #     print(token)
        # if not token:
        #    break
        if token.type == 'NAME':
            name = token.value
        # if token.type == 'NAME':
        #     name = alpha + token.value
        if token.type == 'END':
            # print('\n##############################################\n')
            print(str(name) + ' - OK')
            # print('\n##############################################')
    end = time.time()
    print(end-start)
    print("Main's ending")


class Lexer(object):
    states = (
        ('size', 'exclusive'),
        ('signs', 'exclusive'),
        ('elements', 'exclusive'),
        ('end', 'exclusive'),
        ('equal', 'exclusive'),
        ('figbr', 'exclusive'),
        ('elemmh', 'exclusive'),
        ('endmh', 'exclusive')
    )
    tokens = ('NAME', 'SIGNS', 'SIZE', 'ELEMENTS', 'COMMA', 'END', 'SIZE_ZERO', 'ELEMMH', 'EQUAL', 'FIGBR', 'NL', 'UNKNOWN')

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_NAME(self, t):
        r'^(?m)[a-zA-Z][a-zA-Z\d]{0,15}'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('size')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_size_SIZE(self, t):
        r'\[\d{1,9}\]'
        t.lexer.begin('signs')
        return t

    def t_size_SIZE_ZERO(self, t):
        r'\[0?\]'
        t.lexer.begin('equal')
        return t

    def t_size_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_size_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_signs_SIGNS(self, t):
        r'=\{'
        t.lexer.begin('elements')
        return t

    def t_signs_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_signs_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_elements_ELEMENTS(self, t):
        r'(\-\d+)|(\d+)'
        t.lexer.begin('end')
        return t

    def t_elements_END(self, t):
        r'\}'
        t.lexer.begin('INITIAL')
        return t

    def t_elements_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_elements_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_end_COMMA(self, t):
        r'\,'
        t.lexer.begin('elements')
        return t

    def t_end_END(self, t):
        r'\}'
        t.lexer.begin('INITIAL')
        return t

    def t_end_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_end_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_equal_EQUAL(self, t):
        r'='
        t.lexer.begin('figbr')
        return t

    def t_equal_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_equal_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_figbr_FIGBR(self, t):
        r'\{'
        t.lexer.begin('elemmh')
        return t

    def t_figbr_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_figbr_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_elemmh_ELEMMH(self, t):
        r'(\-?\d+)|(\d+)'
        t.lexer.begin('endmh')
        return t

    def t_elemmh_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_elemmh_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_endmh_COMMA(self, t):
        r'\,'
        t.lexer.begin('elemmh')
        return t

    def t_endmh_END(self, t):
        r'\}'
        t.lexer.begin('INITIAL')
        return t

    def t_endmh_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_endmh_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_size_error(self, t):
        print("Illegal character in size '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_elements_error(self, t):
        print("Illegal character in elements '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_elemmh_error(self, t):
        print("Illegal character in elements '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_figbr_error(self, t):
        print("Illegal character in figure bracket '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_end_error(self, t):
        print("Illegal character in end '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_endmh_error(self, t):
        print("Illegal character in end '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_equal_error(self, t):
        print("Illegal character in equal symbol '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_signs_error(self, t):
        print("Illegal character in signs '%s'" % t.value[0])
        t.lexer.begin('INITIAL')


if __name__ == '__main__':
    main()
