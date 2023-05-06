import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#  主题
from qt_material import apply_stylesheet
#  左右护法
from left import Left
from right import Right

#  继承QMainWindow，状态栏是由QMainWindow创建的



class Main(QMainWindow):

    #  继承父类构造
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #  容器
        self.left = Left(self)
        self.right = Right(self)

        #  窗口大小
        self.setGeometry(300, 300, 800, 600)

        icon = QIcon('cat.jpg')
        self.setWindowIcon(icon)
        self.setWindowTitle('CTF编码/解码器')
        self.show()

    def paintEvent(self, e):
        size = self.size()
        self.left.setGeometry(20, 10, size.width() - 200, size.height()-20)
        self.left.tab.setGeometry(0, 0, self.left.size().width(), self.left.size().height())
        self.right.setGeometry(size.width() - 160, 20, 145, size.height()-40)
        self.right.scroll.setGeometry(0, 0, self.right.size().width(), self.right.size().height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_blue.xml', css_file='custom.css')
    mainwindow = Main()
    sys.exit(app.exec_())
