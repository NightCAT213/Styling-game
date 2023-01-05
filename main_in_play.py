import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice, QChartView
from PyQt5 import QtCore, QtGui, QtWidgets

import main


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   # создаем главное окно
        self.setObjectName("MainWindow")
        self.setGeometry(200, 200, 1607, 780)
        self.setStyleSheet("background-color: rgb(255, 202, 224);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # <Pygame>
        btn_play = QPushButton(self)
        btn_play.setText("Играть")
        btn_play.move(1300, 700)
        btn_play.resize(200, 50)
        btn_play.clicked.connect(self.start_play)
        # </Pygame>

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(60, 130, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 160, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 190, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 90, 16, 161))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(190, 130, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 160, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 190, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 330, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 410, 321, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 670, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 670, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1020, 670, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(249, 630, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(970, 715, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 630, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(390, 10, 781, 651))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1190, 0, 400, 790))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 670, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1607, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # загружаем базу

        self.con = sqlite3.connect("clothes_base.sqlite")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Clothes").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))

        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.radioButton)
        self.buttonGroup.addButton(self.radioButton_2)
        self.buttonGroup.addButton(self.radioButton_3)
        self.buttonGroup.addButton(self.radioButton_4)

        self.pushButton.setStyleSheet("background-color: #fdaac6;")
        self.pushButton_2.setStyleSheet("background-color: #fdaac6;")
        self.pushButton_3.setStyleSheet("background-color: #fdaac6;")
        self.pushButton_4.setStyleSheet("background-color: #fdaac6;")

        self.label.setText("<html><head/><body><p><span style=\" font-size:18pt;\">Сортировка</span></p><p><br/></p></body></html>")
        self.setWindowTitle("Styling Game<3")
        self.radioButton.setText("Платье")
        self.label_2.setText("Тип:")
        self.radioButton_2.setText("Верх")
        self.radioButton_3.setText("Низ")
        self.radioButton_4.setText("Обувь")
        self.label_3.setText("Стиль:")
        self.checkBox.setText("Милый")
        self.checkBox_2.setText("Элегантный")
        self.checkBox_3.setText("Простой")
        self.label_4.setText("Ваш наряд")
        self.pushButton.setText("Сохранить в файл")
        self.pushButton_2.setText("Диаграмма стилей")
        self.pushButton_3.setText("Применить")
        self.pushButton_4.setText("Добавить в наряд")
        self.pushButton_5.setText("Очистить")
        self.pushButton_6.setText("Очистить")
        self.pushButton_7.setText("Показать картинку")
        self.pushButton_8.setText("Удалить последнее")

        self.con = sqlite3.connect("clothes_base.sqlite")
        # активация функций для кнопок
        self.pushButton.clicked.connect(self.save_in_file)
        self.pushButton_2.clicked.connect(self.diagram)
        self.pushButton_3.clicked.connect(self.update_result)
        self.pushButton_4.clicked.connect(self.add_clothe)
        self.pushButton_5.clicked.connect(self.clear_chothes)
        self.pushButton_6.clicked.connect(self.clear_sort)
        self.pushButton_7.clicked.connect(self.show_pic)
        self.pushButton_8.clicked.connect(self.clear_last)

    def start_play(self):
        fd = QFileDialog.getOpenFileName(self, 'Выберите костюм', '/suit')[0]
        f = open(fd, 'r')
        with f:
            data = f.read()
            main.play()

    def clear_last(self):  # удаление последного элемента наряда(кнопка "удалить последнее")
        self.label_6.setText('')
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.movePosition(
            QtGui.QTextCursor.PreviousBlock,
            QtGui.QTextCursor.KeepAnchor, 2)
        cursor.removeSelectedText()
        self.textBrowser.setTextCursor(cursor)

    def save_in_file(self):  # сохранение наряда в файл
        self.label_6.setText('')
        # диалоговое окно для запроса имени файла куда сохранить
        file, ok_pressed = QtWidgets.QInputDialog.getText(self, "Введите название", "Название файла с нарядом")
        if ok_pressed:
            f = open(f'{file}.txt', 'w')
            f.write('Наряд:\n')
            f.write(self.textBrowser.toPlainText())
            f.close()

    def add_clothe(self):  # добавление вещи в наряд
        row = self.tableWidget.currentIndex().row()
        data = [self.tableWidget.item(row, column).text()
                for column in range(self.tableWidget.columnCount())]
        data[-1] = data[-1][12:-4]
        self.textBrowser.append(str('- ' + ', '.join(data) + '\n'))
        self.label_6.setText('')

    def diagram(self):  # создание диаграммы
        m, e, p = 0, 0, 0
        data = self.textBrowser.toPlainText().split('\n') # импорт вещей из текстогого браузера
        self.label_6.setText('')
        for i in data:  # считываем количество вещей определенных типов
            a = i.split(', ')
            if "Милый" in a:
                m += 1
            elif "Элегантный" in a:
                e += 1
            elif "Простой" in a:
                p += 1

        if m == 0 and e == 0 and p == 0:  # проверка на пустоту
            self.label_6.setText('Нет выбранных вещей')

        else:
            series = QPieSeries()

            self.m = round(m / (m + e + p) * 100, 2)
            self.e = round(e / (m + e + p) * 100, 2)
            self.p = round(p / (m + e + p) * 100, 2)

            slice1 = QPieSlice('Милый', self.m)  # элементы будущей диаграммы
            slice1.setExploded(True)
            slice1.setLabelVisible()
            slice1.setColor(QtGui.QColor(255, 202, 224, 255))
            slice1.setLabelBrush(QtGui.QColor(255, 202, 224, 255))
            slice2 = QPieSlice('Элегантный', self.e)
            slice2.setExploded(True)
            slice2.setLabelVisible()
            slice2.setColor(QtGui.QColor(253, 170, 198, 255))
            slice2.setLabelBrush(QtGui.QColor(253, 170, 198, 255))
            slice3 = QPieSlice('Простой', self.p)
            slice3.setExploded(True)
            slice3.setLabelVisible()
            slice3.setColor(QtGui.QColor(252, 121, 164, 255))
            slice3.setLabelBrush(QtGui.QColor(252, 121, 164, 255))

            slices = list()
            slices.append(slice1)
            slices.append(slice2)
            slices.append(slice3)

            series.append(slice1)
            series.append(slice2)
            series.append(slice3)

            chart = QChart()  # сама диаграмма
            chart.legend().hide()
            chart.addSeries(series)
            chart.createDefaultAxes()
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.setTitle('Использованные стили')
            chart.legend().setVisible(True)
            chart.legend().setAlignment(QtCore.Qt.AlignBottom)

            self.chartview = QChartView(chart)  # окно для диаграммы
            self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
            self.chartview.setWindowTitle('Diagramm Of Styles')
            self.chartview.setGeometry(300, 300, 500, 500)
            self.chartview.show()

    def clear_chothes(self):  # очистка текстого браузера полностью
        self.label_6.setText('')
        self.textBrowser.clear()

    def clear_sort(self):  # очистка выбранных радио кнопок и чек-боксов
        self.con = sqlite3.connect("clothes_base.sqlite")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Clothes").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        self.label_6.setText('')
        self.buttonGroup.setExclusive(False)  # очистка радио кнопок

        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)

        self.buttonGroup.setExclusive(True)

        self.checkBox.setChecked(False)  # очистка чек-боксов
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)

    def show_pic(self):  # импорт и показ картинок
        self.label_6.setText('')
        row = self.tableWidget.currentIndex().row()
        if row != -1:
            im = QtGui.QPixmap(self.tableWidget.item(row, 4).text())
            self.label_5.setPixmap(im)

    def update_result(self):  # сортировка и показ базы вещей в тейбл-виджет
        self.label_6.setText('')
        cur = self.con.cursor()
        isCheck = sum([1 if btn.isChecked() else 0 for btn in [self.checkBox, self.checkBox_2, self.checkBox_3]])
        isRadio = sum([1 if btn.isChecked() else 0 for btn in [self.radioButton, self.radioButton_2,
                                                               self.radioButton_3, self.radioButton_4]])
        ch_btn = str()
        ch_btn_2 = str()
        result_2 = list()
        if isCheck != 0:  # есть выбранные стили
            if isRadio != 0: # все выбранно
                if isCheck == 1:  # выбран 1 стиль
                    for btn in [self.checkBox, self.checkBox_2, self.checkBox_3]:
                        if btn.isChecked():
                            ch_btn = btn.text()
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style=? and type=?",
                                           [ch_btn, self.buttonGroup.checkedButton().text()]).fetchall()
                elif isCheck == 2:  # выбранно 2 стиля
                    k = 0
                    for btn in [self.checkBox, self.checkBox_2, self.checkBox_3]:
                        if btn.isChecked() and k == 0:
                            k += 1
                            ch_btn = btn.text()
                        elif btn.isChecked() and k != 0:
                            ch_btn_2 = btn.text()
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style in (?, ?) and type=?",
                                           [ch_btn, ch_btn_2, self.buttonGroup.checkedButton().text()]).fetchall()
                elif isCheck == 3:  # выбрано 3 стиля
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style in (?, ?, ?) and type=?",
                                           [self.checkBox.text(), self.checkBox_2.text(),
                                            self.checkBox_3.text(), self.buttonGroup.checkedButton().text()]).fetchall()
                if result_2:
                    self.tableWidget.setRowCount(len(result_2))
                    self.tableWidget.setColumnCount(len(result_2[0]))
                    for i, elem in enumerate(result_2):
                        for j, val in enumerate(elem):
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                else:
                    self.label_6.setText('По запросу ничего не найдено')
            else:  # выбранны только стили
                if isCheck == 1: # 1 стиль
                    for btn in [self.checkBox, self.checkBox_2, self.checkBox_3]:
                        if btn.isChecked():
                            ch_btn = btn.text()
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style=?", [ch_btn]).fetchall()
                if isCheck == 2:  # 2 стиля
                    k = 0
                    for btn in [self.checkBox, self.checkBox_2, self.checkBox_3]:
                        if btn.isChecked() and k == 0:
                            k += 1
                            ch_btn = btn.text()
                        elif btn.isChecked() and k != 0:
                            ch_btn_2 = btn.text()
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style in (?, ?)", [ch_btn, ch_btn_2]).fetchall()
                if isCheck == 3:  # 3 стиля
                    result_2 = cur.execute("SELECT * FROM Clothes WHERE style in (?, ?, ?)",
                                           [self.checkBox.text(), self.checkBox_2.text(),
                                            self.checkBox_3.text()]).fetchall()
                self.tableWidget.setRowCount(len(result_2))
                self.tableWidget.setColumnCount(len(result_2[0]))
                for i, elem in enumerate(result_2):
                    for j, val in enumerate(elem):
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        else:  # есть выбранные стили
            if isRadio != 0:  # выбран только тип
                result = cur.execute("SELECT * FROM Clothes WHERE type=?", [self.buttonGroup.checkedButton().text()]).fetchall()
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(len(result[0]))
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
            else:  # ничего не выбрано
                pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
