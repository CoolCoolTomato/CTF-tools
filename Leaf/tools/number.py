class Number:
    name = '进制转换'
    value = ''
    char_list = '0123456789abcdefghijklmnopqrstuvwxyz'

    def fun(self, num, fn, tn):
        num = num.lower()
        fn = int(fn)
        tn = int(tn)
        try:
            init_num = int(num, fn)
        except Exception:
            return 'Err'

        while init_num >= tn:
            t = init_num % tn
            self.value = self.char_list[t] + self.value
            init_num = init_num // tn

        self.value = self.char_list[init_num] + self.value
        return self.value

