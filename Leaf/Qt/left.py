from PyQt5.QtWidgets import *
from control import *

class Left(QWidget):
    def __init__(self, father):
        self.father = father
        super().__init__(parent=self.father)
        self.initUI()

    def initUI(self):
        #  标签页
        self.tab = QTabWidget(self)
        self.tab.setMovable(True)
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.onCloseTab)


    def onCloseTab(self, index):
        widget = self.tab.widget(index)
        widget.close()
        self.tab.removeTab(index)

