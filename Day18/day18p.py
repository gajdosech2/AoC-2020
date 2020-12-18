# autor: Lukáš Gajdošech
# uloha: 2. domace zadanie Vyraz

class Vyraz:
    class Stack:
        def __init__(self):
            self._pole = []

        def push(self, data):
            self._pole.append(data)

        def pop(self):
            if self.empty():
                return None
            return self._pole.pop()

        def top(self):
            if self.empty():
                return None
            return self._pole[-1]

        def empty(self):
            return self._pole == []

    def __init__(self):
        self.tabulka = {}

    def __repr__(self):
        ret = ""
        for prvok in self.tabulka:
            ret += prvok + " = " + str(self.tabulka[prvok]) + "\n"
        return ret

    def prirad(self, premenna, vyraz):
        try:
            self.tabulka[premenna] = int(vyraz)
        except ValueError:
            try:
                self.tabulka[premenna] = self.tabulka[vyraz]                #ak je hodnota ina premenna
            except KeyError:
                self.tabulka[premenna] = self.vyhodnot(vyraz)

    def vyhodnot(self, vyraz):
        s = self.Stack()

        if vyraz[0] in '+-*/%':                         #prefixovy zapis
            pole = self.na_pole(vyraz)
            for prvok in reversed(pole):
                if prvok in '+-*/%' and self.pocet_prvkov(s)<2:
                    return None
                if prvok == "+":
                    s.push(s.pop() + s.pop())
                elif prvok == '-':
                    s.push(s.pop() - s.pop())
                elif prvok == '*':
                    s.push(s.pop() * s.pop())
                elif prvok == '/':
                    try:
                        s.push(s.pop() // s.pop())
                    except ZeroDivisionError:
                        return None
                elif prvok == '%':
                    try:
                        s.push(s.pop() % s.pop())
                    except ZeroDivisionError:
                        return None
                elif self.skuska(prvok):
                    try:
                        if self.tabulka[prvok] != None:
                            s.push(self.tabulka[prvok])
                    except KeyError:
                        return None
                else:
                    try:
                        s.push(int(prvok))
                    except ValueError:
                        return None
            if self.pocet_prvkov(s) != 1:
                return None
            return s.pop()

        elif vyraz[len(vyraz)-1] in '+-*/%':                        #postfixovy vyraz
            pole = self.na_pole(vyraz)
            for prvok in pole:
                if prvok in '+-*/%' and self.pocet_prvkov(s)<2:
                    return None
                if prvok == '+':
                    s.push(s.pop() + s.pop())
                elif prvok == '-':
                    s.push(-s.pop() + s.pop())
                elif prvok == '*':
                    s.push(s.pop() * s.pop())
                elif prvok == '/':
                    op2, op1 = s.pop(), s.pop()
                    try:
                        s.push(op1 // op2)
                    except ZeroDivisionError:
                        return None
                elif prvok == '%':
                    op2, op1 = s.pop(), s.pop()
                    try:
                        s.push(op1 % op2)
                    except ZeroDivisionError:
                        return None
                elif self.skuska(prvok):
                    try:
                        if self.tabulka[prvok] != None:
                            s.push(self.tabulka[prvok])
                    except KeyError:
                        return None
                else:
                    try:
                        s.push(int(prvok))
                    except ValueError:
                        return None
            if self.pocet_prvkov(s) != 1:
                return None
            return s.pop()

        else:
            for znak in vyraz:                                      #ak je to vyraz bez operatora
                if znak in '+-*/%':
                    return self.vyhodnot(self.in2post(vyraz))                                 
            return None


    def na_pole(self, vyraz):
        pole, i = [], 0
        vyraz += " "                                                #kvoli IndexError
        while vyraz:
            if vyraz[0] == " ":
                vyraz = vyraz[1:]
            elif vyraz[0] in "+-*/%()":
                pole.append(vyraz[0])
                vyraz = vyraz[1:]
            elif vyraz[0] in "0123456789":
                while vyraz[i] in "0123456789":
                    i += 1
                pole.append(vyraz[0:i])
                vyraz = vyraz[i:]
                i = 0
            elif vyraz[0] in "abcdefghijklmnopqrstuvwxyz":
                while (vyraz[i] in "abcdefghijklmnopqrstuvwxyz") or (vyraz[i] in "0123456789"):
                    i += 1
                pole.append(vyraz[0:i])
                vyraz = vyraz[i:]
                i = 0    
        return pole

    def skuska(self, premenna):
        for znak in premenna:
            if znak in "abcdefghijklmnopqrstuvwxyz":
                return True

    def pocet_prvkov(self, zasobnik):
        pocet = 0
        kopia = self.Stack()
        while not zasobnik.empty():
            kopia.push(zasobnik.pop())
            pocet += 1
        while not kopia.empty():
            zasobnik.push(kopia.pop())
        return pocet

    def in2post(self, vyraz):
        s = self.Stack()
        pole = self.na_pole(vyraz)
        vystup = ""
        for prvok in pole:

            if prvok in '+-':
                if s.empty():
                    s.push(prvok)
                else:
                    while s.top() in '+-':
                        vystup += s.pop() + " "
                        if s.top() == None:
                            break
                    s.push(prvok)

            elif prvok in '*/%':
                if s.empty():
                    s.push(prvok)
                else:
                    while s.top() in '+-*/%':
                        vystup += s.pop() + " "
                        if s.top() == None:
                            break
                    s.push(prvok)
                    
            elif prvok == "(":
                s.push(prvok)
                
            elif prvok == ")":
                while s.top() != "(":
                    if s.empty():
                        return ""
                    vystup += s.pop() + " "
                s.pop()                                 #vyhodim pravu zatvorku

            else:
                vystup += prvok + " "

        while not s.empty():
            vystup += s.pop() + " "

        return vystup[0:len(vystup)-1]


with open("day18.txt") as day_file:
    line = day_file.readline().strip()
    summ = 0
    v = Vyraz()
    while line:
        summ += v.vyhodnot(line)
        line = day_file.readline().strip()

    print(summ)
