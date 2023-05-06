import numpy as np


class Hill:

    def __init__(self):
        self.text = ''
        self.key = ''
        self.mod1 = ''
        self.mod2 = ''
        self.value = ''

    def __call__(self, text, key, mod1, mod2):
        self.text = text.upper()
        self.key = key.upper()
        self.mod1 = str(mod1)
        self.mod2 = str(mod2)

        #  合法性判断
        if self.valid(self.text, self.key):
            pass
        else:
            return 'Err'

        #  转换为矩阵
        self.text, self.key = self.str2matrix(self.text, self.key, self.mod2)

        #  密钥合法性
        if self.is_key_valid(self.key):
            pass
        else:
            return '密钥不可逆'

        #  加密和解密
        if self.mod1 == '0':
            return self.encode(self.text, self.key, self.mod2)

        elif self.mod1 == '1':
            return self.decode(self.text, self.key, self.mod2)

    def valid(self, text, key):
        #  判断内容是否合法
        if text == '':
            return False
        if key == '':
            return False
        l = int(len(key) ** 0.5)
        if l ** 2 != len(key):
            return False
        #  True
        return True

    def str2matrix(self, text, key, mod2):
        #  获取矩阵宽高
        w = int(len(key)**0.5)
        if len(text) % w == 0:
            h = len(text) // w
        else:
            h = (len(text) // w) + 1
        matrix_text = [[0 for _ in range(w)] for _ in range(h)]
        matrix_key = [[0 for _ in range(w)] for _ in range(w)]
        #  转换
        if mod2 == '0':
            for i in range(len(text)):
                matrix_text[i // w][i % w] = (ord(text[i]) - 65) % 26
            for j in range(len(key)):
                matrix_key[j // w][j % w] = (ord(key[j]) - 65) % 26
            return matrix_text, matrix_key
        elif mod2 == '1':
            for i in range(len(text)):
                matrix_text[i // w][i % w] = (ord(text[i]) - 64) % 26
            for j in range(len(key)):
                matrix_key[j // w][j % w] = (ord(key[j]) - 64) % 26
            return matrix_text, matrix_key
        else:
            pass

    def is_key_valid(self, key):
        try:
            key = np.linalg.inv(np.array(key))
        except Exception:
            return False
        return True

    def encode(self, text, key, mod2):
        self.value = ''
        text = np.array(text)
        key = np.array(key)
        value = np.matmul(text, key)
        if mod2 == '0':
            for i in value:
                for j in i:
                    self.value += chr((j % 26) + 65)
        elif mod2 == '1':
            for i in value:
                for j in i:
                    self.value += chr(((j-1) % 26) + 65)
        else:
            pass
        return self.value

    def decode(self, text, key, mod2):
        self.value = ''
        text = np.array(text)
        key = np.array(key)
        key = np.linalg.inv(key)
        value = np.matmul(text, key)
        if mod2 == '0':
            for i in value:
                for j in i:
                    self.value += chr(int(j) % 26 + 65)
        elif mod2 == '1':
            for i in value:
                for j in i:
                    self.value += chr(int(j - 1) % 26 + 65)
        else:
            pass
        return self.value

