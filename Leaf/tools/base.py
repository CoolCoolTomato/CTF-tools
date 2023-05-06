import base64
import base58
import base36
import base91


class BaseBase:
    name = ''
    value = ''

    def encode(self, text):
        pass

    def decode(self, text):
        pass


class Base91(BaseBase):
    name = 'Base91'
    value = ''

    def encode(self, text):
        try:
            self.value = base91.encode(text.encode('utf-8'))
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base91.decode(text.decode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value


class Base85(BaseBase):
    name = 'Base85'
    value = ''

    def encode(self, text):
        try:
            self.value = base64.b85encode(text.encode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base64.b85decode(text).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value


class Base64(BaseBase):
    name = 'Base64'
    value = ''

    def encode(self, text):
        try:
            self.value = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base64.b64decode(text).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value


class Base58(BaseBase):
    name = 'Base58'
    value = ''

    def encode(self, text):
        try:
            self.value = base58.b58encode(text.encode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base58.b58decode(text).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value


class Base36(BaseBase):
    name = 'Base36'
    value = ''

    def encode(self, text):
        try:
            self.value = base36.loads(text)
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base36.dumps(int(text))
        except Exception:
            self.value = 'Err'
        return self.value


class Base32(BaseBase):
    name = 'Base32'
    value = ''

    def encode(self, text):
        try:
            self.value = base64.b32encode(text.encode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base64.b32decode(text).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value


class Base16(BaseBase):
    name = 'Base16'
    value = ''

    def encode(self, text):
        try:
            self.value = base64.b16encode(text.encode('utf-8')).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

    def decode(self, text):
        try:
            self.value = base64.b16decode(text).decode('utf-8')
        except Exception:
            self.value = 'Err'
        return self.value

