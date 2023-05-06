class Caesar:
    name = 'caesar'
    value = ''

    def encode(self, text, flag):
        for c in text:
            if ord('a') <= ord(c) <= ord('z'):
                self.value += chr((ord(c) - ord('a') + int(flag)) % 26 + ord('a'))
            elif ord('A') <= ord(c) <= ord('Z'):
                self.value += chr((ord(c) - ord('A') + int(flag)) % 26 + ord('A'))
            else:
                return 'Err'
        return self.value

    def decode(self, text, flag):
        for c in text:
            if ord('a') <= ord(c) <= ord('z'):
                self.value += chr((ord(c) - ord('a') - int(flag)) % 26 + ord('a'))
            elif ord('A') <= ord(c) <= ord('Z'):
                self.value += chr((ord(c) - ord('A') - int(flag)) % 26 + ord('A'))
            else:
                return 'Err'
        return self.value

