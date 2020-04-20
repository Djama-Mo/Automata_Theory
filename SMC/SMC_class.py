import smc_project_sm
import string
import time

directory = '/home/djama/Рабочий стол'


def main():
    print('Main function is beginning\n')
    tmp = SMC_project()
    gen_strings_file = open(directory + '/templates.txt', 'r')
    result = open(directory + '/smc_result.txt', '+a')
    start = time.time()
    for line in gen_strings_file.readlines():
        match = tmp.CheckString(line.rstrip())
    end = time.time()
    print(end - start)
    for key in tmp.result.keys():
        result.write(key + ' ')
        result.write(str(tmp.result[key]) + '\n')
    result.close()
    gen_strings_file.close()
    print('Main function is ending\n')


class SMC_project(object):

    def __init__(self):
        self._fsm = smc_project_sm.Appclass_sm(self)
        self._count = 0
        self._name = ''
        self._elemcount = ''
        self._elements = ''
        self._is_acceptable = True
        self._result = {}
        self._fsm.enterStartState()
        self.sv = ''

    def CheckString(self, text):
        self._fsm.Array()
        for c in text:
            if not self._is_acceptable:
                break
            if c in string.ascii_letters:
                self._fsm.Letter(c)
            elif c in string.digits:
                self._fsm.Digit(c)
            elif c == ',':
                self._fsm.CommaSym(c)
            elif c == '{' or c == '}':
                self._fsm.FigBracketSym()
            elif c == '[' or c == ']':
                self._fsm.SqBracketSym()
            elif c == '=':
                self._fsm.EqSym()
            elif c == '-':
                self._fsm.Minus(c)
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        self.AddToDict(self.sv)
        return self._is_acceptable, self.sv

    def AddToDict(self, key):
        if not self._is_acceptable:
            return
        if self._result.get(key) is None:
            self._result[key] = 1
        else:
            num = self._result.get(key)
            self._result[key] = num + 1

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def CountZero(self):
        self._count = 0

    def CountInc(self):
        self._count += 1

    def ClearSMC(self):
        self._is_acceptable = True
        self._count = 0
        self._name = ''
        self._elemcount = ''
        self._elements = ''
        self.sv = ''

    def ClearMemory(self):
        self._name = ''

    def SaveName(self):
        self.sv = self._name
        self._name = ''

    def Memorise(self, letter):
        self._name += letter

    def NonZero(self):
        return self._count != 0

    def FirstAlpha(self):
        try:
            sym = self._name[0]
            if sym in string.ascii_letters:
                return True
            else:
                return False
        except IndexError:
            return False

    def CheckName(self):
        if self.FirstAlpha() and len(self._name) <= 16:
            return True
        else:
            return False

    def MemoriseCnt(self, letter):
        self._elemcount += letter

    def CheckCount(self):
        return len(self._elemcount) <= 9

    def NecEl(self):
        if self._elemcount is '':
            tmp = self.NonZero()
            return tmp
        else:
            return True

    def MemoriseElem(self, letter):
        self._elements += letter

    @staticmethod
    def Printok():
        print('Ok')

    @staticmethod
    def Printerror():
        print('Error')

    @property
    def result(self):
        return self._result

    def Null(self):
        self._result = {}

    def PrintDict(self):
        for key, item in self._result.items():
            print(key + ' - ' + str(item))

    def SaveTime(self, times, number):
        f = open(directory + "time.txt", '+a')
        f.write(str(times) + '\n')
        f.write(str(number))
        f.close()
        self.Null()


if __name__ == "__main__":
    main()
