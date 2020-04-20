import ply.lex as lex


def main():
    print("Main's starting")
    file = open('templates_tmp.txt', 'r')
    tmp = file.read()
    file.close()
    lexer = Lexer()
    lexer.input(tmp)
    while True:
        token = lexer.token()
        print(token)
        if not token:
            break
        if token.type == 'ALPHA':
            alpha = token.value
        if token.type == 'NAME':
            print('\n##############################################\n')
            print(token.type, alpha + token.value)
            print('\n##############################################\n')
        if token.type == 'NL':
            print('\n')
    print("Main's ending")


class Lexer(object):
    states = (
        ('name', 'exclusive'),
        ('size', 'exclusive'),
        ('elements', 'exclusive'),
        ('elemmh', 'exclusive')
    )
    tokens = ('ALPHA', 'NAME', 'SIZE', 'SIZE_ZERO', 'ELEMMH', 'ELEMENTS', 'NL', 'UNKNOWN')

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_ALPHA(self, t):
        r'^(?m)[a-zA-Z]'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('name')
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

    def t_name_NAME(self, t):
        r'([a-zA-Z\d]{1,15})'
        t.lexer.begin('size')
        return t

    def t_name_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_name_UNKNOWN(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_size_SIZE(self, t):
        r'\[\d{1,9}\]'
        t.lexer.begin('elements')
        return t

    def t_size_SIZE_ZERO(self, t):
        r'\[\]'
        t.lexer.begin('elemmh')
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

    def t_elements_ELEMENTS(self, t):
        r'=\{(\-*\d*\,*)+\}'
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

    def t_elemmh_ELEMENTS(self, t):
        r'=\{(\-*\d+\,*)+\}'
        t.lexer.begin('INITIAL')
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

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_name_error(self, t):
        print("Illegal character in name '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_size_error(self, t):
        print("Illegal character in size'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_elements_error(self, t):
        print("Illegal character in elements'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_elemmh_error(self, t):
        print("Illegal character in elements'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

if __name__ == '__main__':
    main()
