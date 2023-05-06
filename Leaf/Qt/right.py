from PyQt5.QtWidgets import *
from control import *
from copy import deepcopy
from PyQt5.QtCore import pyqtSignal


class Right(QWidget):
    def __init__(self, father):
        self.father = father
        super().__init__(parent=self.father)
        self.initUI()

    def initUI(self):
        #  滚动区
        self.scroll = QScrollArea(self)
        bar = QWidget()

        self.register = Index.__subclasses__()
        self.register_list = [c.name for c in self.register]
        self.register_dict = dict(zip(self.register_list, self.register))

        rightlayout = QVBoxLayout(bar)
        rightlayout.setSpacing(10)

        for name in self.register_list:
            button = MyButton(name, self)
            rightlayout.addWidget(button)

        bar.setLayout(rightlayout)
        self.scroll.setWidget(bar)


class MyButton(QPushButton):
    my_signal = pyqtSignal(str)

    def __init__(self, name, parent):
        self.parent = parent
        super(MyButton, self).__init__(text=name, parent=parent)
        self.my_signal.connect(self.addcontrol)

    def addcontrol(self, name):
        control = self.parent.register_dict[name]
        example = control(self.parent.father.left)
        self.parent.father.left.tab.addTab(example, example.name)

    def mousePressEvent(self, event):
        name = self.text()
        self.my_signal.emit(str(name))
