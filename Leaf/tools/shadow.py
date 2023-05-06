class Shadow:
    value = ''

    def decode(self, text):
        if self.check(text):
            pass
        else:
            return 'Err'
        value_list = text.split('0')
        for block in value_list:
            num = 0
            for i in block:
                num += int(i)
            try:
                self.value += chr(ord('a') + num -1)
            except Exception:
                return 'Err'
        return self.value



    def check(self, text):
        num_list = ['0', '1', '2', '4', '8']
        for i in text:
            if i not in num_list:
                return False
        else:
            return True