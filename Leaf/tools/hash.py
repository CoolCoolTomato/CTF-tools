import hashlib


class HashBase:
    name = ''
    value = ''

    def encode(self, text):
        pass


class Md5(HashBase):
    name = 'Md5'
    value = ''

    def encode(self, text):
        e = hashlib.md5()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value


class Sha1(HashBase):
    name = 'Sha1'
    value = ''

    def encode(self, text):
        e = hashlib.sha1()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value


class Sha224(HashBase):
    name = 'Sha224'
    value = ''

    def encode(self, text):
        e = hashlib.sha224()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value


class Sha256(HashBase):
    name = 'Sha256'
    value = ''

    def encode(self, text):
        e = hashlib.sha256()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value


class Sha384(HashBase):
    name = 'Sha384'
    value = ''

    def encode(self, text):
        e = hashlib.sha384()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value


class Sha512(HashBase):
    name = 'Sha512'
    value = ''

    def encode(self, text):
        e = hashlib.sha512()
        e.update(text.encode('utf-8'))
        self.value = e.hexdigest()
        return self.value

