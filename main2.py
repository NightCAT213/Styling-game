import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(527, 572)
        self.setStyleSheet("background-color: rgb(255, 197, 233);")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(330, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 233, 242);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 300, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 233, 242);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(330, 360, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 541))
        self.label.setObjectName("label")

        self.setWindowTitle("Просмотр персонажа")
        self.pushButton.setText("Загрузить наряд")
        self.pushButton_2.setText("Продолжить")

        self.pushButton.clicked.connect(self.getfiles)
        self.pushButton_2.clicked.connect(self.translate)
        self.counter = 0
        self.file = 0

    def getfiles(self):
        self.textBrowser.setText('')
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Text files (*.txt)")
        f = open(str(fname[0]), 'r')
        if f.read(6) == 'Наряд:':
            f.seek(6)
            lst = f.readlines()
            data = []
            for i in lst:
                if i != '\n':
                    data.append(i.split(', '))
            pl, v, n, ob = 0, 0, 0, 0
            if len(data) <= 3:
                for i in data:
                    if i[0] == '- Верх':
                        v += 1
                    elif i[0] == '- Низ':
                        n += 1
                    elif i[0] == '- Платье':
                        pl += 1
                    elif i[0] == '- Обувь':
                        ob += 1
                    else:
                        self.textBrowser.setText('Файл не удовлетворяет форматам игры')
                        break
                if ((len(data) == 3 and v == 1 and n == 1 and ob == 1)
                    or (len(data) == 2 and ((pl == 1 and ob == 1) or (v == 1 or n == 1 or ob == 1)))
                        or (len(data) == 1)):
                    self.counter += 1
                    img = Image.open('images_game2/doll.png')
                    for i in data:
                        fn = Image.open(str('images_game2/' + i[-1][:-1] + '.png'))
                        img.paste(fn, (0, 0), mask=fn)
                    img.save(str(fname[0])[:-4] + '_' + str(self.counter) + ".png")
                    im = QtGui.QPixmap(str(fname[0])[:-4] + '_' + str(self.counter) + ".png")
                    im = im.scaled(271, 521)
                    self.label.setPixmap(im)
                    self.file = str(fname[0])[:-4] + '_' + str(self.counter) + ".png"
                else:
                    self.textBrowser.setText('Файл не удовлетворяет форматам игры')
            else:
                self.textBrowser.setText('Файл не удовлетворяет форматам игры')
        else:
            self.textBrowser.setText('Файл не удовлетворяет форматам игры')

    def translate(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
