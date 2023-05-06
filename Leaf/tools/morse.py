class Morse:
    dic = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
           'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
           'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
           'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
           'Y': '_.__', 'Z': '__..',
           '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
           '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
           ' ': ' '}
    dic_rev = dict(zip(dic.values(), dic.keys()))

    value = ''

    #  sign1 = '.'
    #  sign2= '_'
    #  sign3 = ' '
    def encode(self, text, sign1, sign2, sign3):
        self.value = ''
        text = text.upper()
        if self.check_sign(sign1, sign2, sign3):
            pass
        else:
            return 'Err'
        signs = list(text)
        for s in signs:
            try:
                self.value += self.dic[s]
                self.value += ' '
            except Exception:
                return 'Err'
        self.value = self.value.replace('.', sign1)
        self.value = self.value.replace('_', sign2)
        self.value = self.value.replace(' ', sign3)
        return self.value

    def decode(self, text, sign1, sign2, sign3):
        self.value = ''
        if self.check_sign(sign1, sign2, sign3):
            pass
        else:
            return 'Err'
        text = text.replace(sign1, '.')
        text = text.replace(sign2, '_')
        text = text.replace(sign3, ' ')
        signs = text.split(' ')
        if '' in signs:
            signs.remove('')
        for s in signs:
            try:
                self.value += self.dic_rev[s]
            except Exception:
                return 'Err'
        return self.value

    def check_sign(self, sign1, sign2, sign3):
        if sign1 == sign2:
            return False

        elif sign2 == sign3:
            return False

        elif sign3 == sign1:
            return False
        else:
            return True

