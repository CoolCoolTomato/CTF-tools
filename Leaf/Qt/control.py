from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from tools.base import *
from tools.hash import *
from tools.hill import Hill
from tools.number import Number
from tools.shadow import Shadow
from tools.caesar import Caesar
from tools.morse import Morse
from tools.sizelen import Sizelen


class Index:
    name = ''


class Bases(QWidget, Index):
    name = 'Base'

    def __init__(self, father):
        super(Bases, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        classes = BaseBase.__subclasses__()
        self.classes_dic = dict(zip([c.name for c in classes],  classes))
        self.now = classes[2]

        combo = QComboBox(self)
        for c in classes:
            combo.addItem(c.name)
        combo.setCurrentIndex(2)
        combo.activated[str].connect(self.handle)

        encode_button = QPushButton('加密')
        decode_button = QPushButton('解密')
        encode_button.clicked.connect(self.encode)
        decode_button.clicked.connect(self.decode)

        hlayout = QHBoxLayout()
        hlayout.addWidget(combo)
        hlayout.addWidget(encode_button)
        hlayout.addWidget(decode_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def handle(self, name):
        self.now = self.classes_dic[name]

    def encode(self):
        encode_text = self.encrypt_text.toPlainText()
        result = str(self.now().encode(encode_text))
        self.result_text.setPlainText(result)

    def decode(self):
        decode_text = self.encrypt_text.toPlainText()
        result = str(self.now().decode(decode_text))
        self.result_text.setPlainText(result)


class Hashs(QWidget, Index):
    name = 'hash'

    def __init__(self, father):
        super(Hashs, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        classes = HashBase.__subclasses__()
        self.classes_dic = dict(zip([c.name for c in classes],  classes))
        self.now = classes[0]

        combo = QComboBox(self)
        for c in classes:
            combo.addItem(c.name)
        combo.setCurrentIndex(2)
        combo.activated[str].connect(self.handle)

        encode_button = QPushButton('加密')
        encode_button.clicked.connect(self.encode)

        hlayout = QHBoxLayout()
        hlayout.addWidget(combo)
        hlayout.addWidget(encode_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def handle(self, name):
        self.now = self.classes_dic[name]

    def encode(self):
        encode_text = self.encrypt_text.toPlainText()
        result = str(self.now().encode(encode_text))
        self.result_text.setPlainText(result)


class Hills(QWidget, Index):
    name = 'Hill'

    def __init__(self, father):
        super(Hills, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        self.hill = Hill()

        self.combo = QComboBox(self)
        self.combo.addItem('A=0')
        self.combo.addItem('A=1')
        encode_button = QPushButton('加密')
        decode_button = QPushButton('解密')
        encode_button.clicked.connect(self.encode)
        decode_button.clicked.connect(self.decode)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.combo)
        hlayout1.addWidget(encode_button)
        hlayout1.addWidget(decode_button)

        label = QLabel('密钥:')
        self.key = QLineEdit()

        halyout2 = QHBoxLayout()
        halyout2.addWidget(label)
        halyout2.addWidget(self.key)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(halyout2)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def encode(self):
        encode_text = self.encrypt_text.toPlainText()
        key_text = self.key.text()
        mod1 = 0
        mod2 = self.combo.currentText()[-1]
        result = self.hill(encode_text, key_text, mod1, mod2)
        self.result_text.setPlainText(result)

    def decode(self):
        decode_text = self.encrypt_text.toPlainText()
        key_text = self.key.text()
        mod1 = 1
        mod2 = self.combo.currentText()[-1]
        result = self.hill(decode_text, key_text, mod1, mod2)
        self.result_text.setPlainText(result)


class Numbers(QWidget, Index):
    name = '进制转换'

    def __init__(self, father):
        super(Numbers, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        from_label = QLabel('from:')
        from_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.fn = QComboBox(self)
        for i in range(2, 37):
            self.fn.addItem(str(i))

        to_label = QLabel('to:')
        to_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tn = QComboBox(self)
        for j in range(2, 37):
            self.tn.addItem(str(j))

        encode_button = QPushButton('Run!')
        encode_button.clicked.connect(self.run)

        hlayout = QHBoxLayout()
        hlayout.addWidget(from_label)
        hlayout.addWidget(self.fn)
        hlayout.addWidget(to_label)
        hlayout.addWidget(self.tn)
        hlayout.addWidget(encode_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def run(self):
        number = self.encrypt_text.toPlainText()
        fn = self.fn.currentText()
        tn = self.tn.currentText()
        result = Number().fun(number, fn, tn)
        self.result_text.setPlainText(result)


class Shadows(QWidget, Index):
    name = '云影密码'

    def __init__(self, father):
        super(Shadows, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        label = QLabel('云影密码:')
        button = QPushButton('解密')
        button.clicked.connect(self.decode)

        hlayout = QHBoxLayout()
        hlayout.addWidget(label)
        hlayout.addWidget(button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def decode(self):
        encrypt = self.encrypt_text.toPlainText()
        result = Shadow().decode(encrypt)
        self.result_text.setPlainText(result)


class Caesars(QWidget, Index):
    name = '凯撒密码'

    def __init__(self, father):
        super(Caesars, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        label = QLabel('偏移量:')
        self.flag = QLineEdit()
        encode_button = QPushButton('加密')
        encode_button.clicked.connect(self.encode)
        decode_button = QPushButton("解密")
        decode_button.clicked.connect(self.decode)

        hlayout = QHBoxLayout()
        hlayout.addWidget(label)
        hlayout.addWidget(self.flag)
        hlayout.addWidget(encode_button)
        hlayout.addWidget(decode_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def encode(self):
        encrypt = self.encrypt_text.toPlainText()
        flag = self.flag.text()
        result = Caesar().encode(encrypt, flag)
        self.result_text.setPlainText(result)

    def decode(self):
        encrypt = self.encrypt_text.toPlainText()
        flag = self.flag.text()
        result = Caesar().decode(encrypt, flag)
        self.result_text.setPlainText(result)


class Morses(QWidget, Index):
    name = '摩斯密码'

    def __init__(self, father):
        super(Morses, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        sign1 = QLabel('短符号:')
        self.sign1_text = QLineEdit()
        self.sign1_text.setText('.')
        sign2 = QLabel('长符号:')
        self.sign2_text = QLineEdit()
        self.sign2_text.setText('_')
        sign3 = QLabel('分隔符:')
        self.sign3_text = QLineEdit()
        self.sign3_text.setText(' ')

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(sign1)
        hlayout1.addWidget(self.sign1_text)
        hlayout1.addWidget(sign2)
        hlayout1.addWidget(self.sign2_text)
        hlayout1.addWidget(sign3)
        hlayout1.addWidget(self.sign3_text)

        encode_button = QPushButton('加密')
        encode_button.clicked.connect(self.encode)
        decode_button = QPushButton("解密")
        decode_button.clicked.connect(self.decode)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(encode_button)
        hlayout2.addWidget(decode_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def encode(self):
        encrypt = self.encrypt_text.toPlainText()
        sign1 = self.sign1_text.text()
        sign2 = self.sign2_text.text()
        sign3 = self.sign3_text.text()
        result = Morse().encode(encrypt, sign1, sign2, sign3)
        self.result_text.setPlainText(result)

    def decode(self):
        encrypt = self.encrypt_text.toPlainText()
        sign1 = self.sign1_text.text()
        sign2 = self.sign2_text.text()
        sign3 = self.sign3_text.text()
        result = Morse().decode(encrypt, sign1, sign2, sign3)
        self.result_text.setPlainText(result)


class Sizelens(QWidget, Index):
    name = '字符串操作'

    def __init__(self, father):
        super(Sizelens, self).__init__(parent=father)
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.encrypt_text = QTextEdit()
        self.result_text = QTextEdit()

        big_button = QPushButton('大写')
        big_button.clicked.connect(self.tobig)
        small_button = QPushButton("小写")
        small_button.clicked.connect(self.tosmall)
        len_button = QPushButton("长度")
        len_button.clicked.connect(self.getlen)


        hlayout = QHBoxLayout()
        hlayout.addWidget(big_button)
        hlayout.addWidget(small_button)
        hlayout.addWidget(len_button)

        vlayout.addWidget(self.encrypt_text)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.result_text)
        vlayout.setSpacing(10)
        self.setLayout(vlayout)

    def tobig(self):
        encrypt = self.encrypt_text.toPlainText()
        result = Sizelen().big(encrypt)
        self.result_text.setPlainText(result)

    def tosmall(self):
        encrypt = self.encrypt_text.toPlainText()
        result = Sizelen().small(encrypt)
        self.result_text.setPlainText(result)

    def getlen(self):
        encrypt = self.encrypt_text.toPlainText()
        result = Sizelen().lens(encrypt)
        self.result_text.setPlainText(result)


