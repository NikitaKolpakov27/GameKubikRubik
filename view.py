import sys
from random import randint

from sys import argv, executable
import os

from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QPen, QColor, QMouseEvent
from PyQt5.QtWidgets import QWidget

import game



class Example(QtWidgets.QWidget):
    YELLOW = "ffff00"
    BLUE = "0000ff"
    GREEN = "008000"
    RED = "ff0000"
    EXIT_CODE_REBOOT = -123

    def __init__(self):
        super().__init__()
        self.initUI()

    def action_cube_right_1(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][0]
        data1[0][1] = cube_full[0][1]
        data1[1][0] = cube_full[1][0]
        data1[1][1] = cube_full[1][1]

        data1 = game.list_rot_right(data1)
        cube_full[0][0] = data1[0][0]
        cube_full[0][1] = data1[0][1]
        cube_full[1][0] = data1[1][0]
        cube_full[1][1] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_left_1(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][0]
        data1[0][1] = cube_full[0][1]
        data1[1][0] = cube_full[1][0]
        data1[1][1] = cube_full[1][1]

        data1 = game.list_rot_left(data1)
        cube_full[0][0] = data1[0][0]
        cube_full[0][1] = data1[0][1]
        cube_full[1][0] = data1[1][0]
        cube_full[1][1] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_left_2(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][2]
        data1[0][1] = cube_full[0][3]
        data1[1][0] = cube_full[1][2]
        data1[1][1] = cube_full[1][3]

        data1 = game.list_rot_left(data1)
        cube_full[0][2] = data1[0][0]
        cube_full[0][3] = data1[0][1]
        cube_full[1][2] = data1[1][0]
        cube_full[1][3] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_right_2(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][2]
        data1[0][1] = cube_full[0][3]
        data1[1][0] = cube_full[1][2]
        data1[1][1] = cube_full[1][3]

        data1 = game.list_rot_right(data1)
        cube_full[0][2] = data1[0][0]
        cube_full[0][3] = data1[0][1]
        cube_full[1][2] = data1[1][0]
        cube_full[1][3] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_left_3(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][0]
        data1[0][1] = cube_full[2][1]
        data1[1][0] = cube_full[3][0]
        data1[1][1] = cube_full[3][1]

        data1 = game.list_rot_left(data1)
        cube_full[2][0] = data1[0][0]
        cube_full[2][1] = data1[0][1]
        cube_full[3][0] = data1[1][0]
        cube_full[3][1] = data1[1][1]

        game.cube_full = cube_full


    def action_cube_right_3(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][0]
        data1[0][1] = cube_full[2][1]
        data1[1][0] = cube_full[3][0]
        data1[1][1] = cube_full[3][1]

        data1 = game.list_rot_right(data1)
        cube_full[2][0] = data1[0][0]
        cube_full[2][1] = data1[0][1]
        cube_full[3][0] = data1[1][0]
        cube_full[3][1] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_right_4(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][2]
        data1[0][1] = cube_full[2][3]
        data1[1][0] = cube_full[3][2]
        data1[1][1] = cube_full[3][3]

        data1 = game.list_rot_right(data1)
        cube_full[2][2] = data1[0][0]
        cube_full[2][3] = data1[0][1]
        cube_full[3][2] = data1[1][0]
        cube_full[3][3] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_left_4(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][2]
        data1[0][1] = cube_full[2][3]
        data1[1][0] = cube_full[3][2]
        data1[1][1] = cube_full[3][3]

        data1 = game.list_rot_left(data1)
        cube_full[2][2] = data1[0][0]
        cube_full[2][3] = data1[0][1]
        cube_full[3][2] = data1[1][0]
        cube_full[3][3] = data1[1][1]

        game.cube_full = cube_full

    def action_cube_center_left(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[1][1]
        data1[0][1] = cube_full[1][2]
        data1[1][0] = cube_full[2][1]
        data1[1][1] = cube_full[2][2]

        data1 = game.list_rot_left(data1)
        cube_full[1][1] = data1[0][0]
        cube_full[1][2] = data1[0][1]
        cube_full[2][1] = data1[1][0]
        cube_full[2][2] = data1[1][1]

        game.cube_full = cube_full


    def action_cube_center_right(self):
        self.updateFrame()
        cube_full = game.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[1][1]
        data1[0][1] = cube_full[1][2]
        data1[1][0] = cube_full[2][1]
        data1[1][1] = cube_full[2][2]

        data1 = game.list_rot_right(data1)
        cube_full[1][1] = data1[0][0]
        cube_full[1][2] = data1[0][1]
        cube_full[2][1] = data1[1][0]
        cube_full[2][2] = data1[1][1]

        game.cube_full = cube_full


    def setFullCube(self):
        cube_full = [["к", "к" ,"з" ,"з"], ["к", "к", "з", "з"], ["ж", "ж", "с", "с"], ["ж","ж" ,"с" ,"с"]]
        game.cube_full = cube_full
        self.updateFrame()

    def mousePressEvent(self, ev):
        cube = game.cube_full
        position = ev.pos()

        """[0][0]"""
        if (position.x() >= 300 and position.x() <= 400 and position.y() >= 100 and position.y() <= 200):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_1()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_1()
                self.updateFrame()
                #return QWidget.mousePressEvent(self, ev)
            # return QWidget.mousePressEvent(self, ev)

        """[0][1]"""
        if (position.x() >= 400 and position.x() <= 500 and position.y() >= 100 and position.y() <= 200):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_1()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_1()
                self.updateFrame()

        """[0][2]"""
        if (position.x() >= 500 and position.x() <= 600 and position.y() >= 100 and position.y() <= 200):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_2()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_2()
                self.updateFrame()

        """[0][3]"""
        if (position.x() >= 600 and position.x() <= 700 and position.y() >= 100 and position.y() <= 200):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_2()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_2()
                self.updateFrame()

        """[1][0]"""
        if (position.x() >= 300 and position.x() <= 400 and position.y() >= 200 and position.y() <= 300):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_1()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_1()
                self.updateFrame()

        """[1][1]"""
        if (position.x() >= 400 and position.x() <= 500 and position.y() >= 200 and position.y() <= 300):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_center_left()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_center_right()
                self.updateFrame()

        """[1][2]"""
        if (position.x() >= 500 and position.x() <= 600 and position.y() >= 200 and position.y() <= 300):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_center_left()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_center_right()
                self.updateFrame()

        """[1][3]"""
        if (position.x() >= 600 and position.x() <= 700 and position.y() >= 200 and position.y() <= 300):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_2()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_2()
                self.updateFrame()

        """[2][0]"""
        if (position.x() >= 300 and position.x() <= 400 and position.y() >= 300 and position.y() <= 400):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_3()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_3()
                self.updateFrame()

        """[2][1]"""
        if (position.x() >= 400 and position.x() <= 500 and position.y() >= 300 and position.y() <= 400):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_center_left()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_center_right()
                self.updateFrame()

        """[2][2]"""
        if (position.x() >= 500 and position.x() <= 600 and position.y() >= 300 and position.y() <= 400):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_center_left()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_center_right()
                self.updateFrame()

        """[2][3]"""
        if (position.x() >= 600 and position.x() <= 700 and position.y() >= 300 and position.y() <= 400):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_4()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_4()
                self.updateFrame()

        """[3][0]"""
        if (position.x() >= 300 and position.x() <= 400 and position.y() >= 400 and position.y() <= 500):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_3()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_3()
                self.updateFrame()

        """[3][1]"""
        if (position.x() >= 400 and position.x() <= 500 and position.y() >= 400 and position.y() <= 500):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_3()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_3()
                self.updateFrame()

        """[3][2]"""
        if (position.x() >= 500 and position.x() <= 600 and position.y() >= 400 and position.y() <= 500):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_4()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_4()
                self.updateFrame()

        """[3][3]"""
        if (position.x() >= 600 and position.x() <= 700 and position.y() >= 400 and position.y() <= 500):
            if ev.button() == Qt.LeftButton:
                ev.accept()
                print(position.x())
                self.action_cube_left_4()
                self.updateFrame()
            else:
                ev.accept()
                print(position.x())
                self.action_cube_right_4()
                self.updateFrame()

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent = None) -> None:
        if me.button() == Qt.LeftButton:
            self._game.left_mouse_click(e.row(), e.column())
        elif me.button() == Qt.RightButton:
            self._game.right_mouse_click(e.row(), e.column())
        self.update_view()



    def initUI(self):
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Colours')

        # """1-я грань"""
        # btn = QtWidgets.QPushButton(self)
        # btn.move(170, 150)
        # btn.setText("Влево")
        # btn.clicked.connect(self.action_cube_left_1)
        #
        # btn = QtWidgets.QPushButton(self)
        # btn.move(370, 40)
        # btn.setText("Вправо")
        # btn.clicked.connect(self.action_cube_right_1)
        #
        # """2-я грань"""
        # btn = QtWidgets.QPushButton(self)
        # btn.move(570, 40)
        # btn.setText("Влево")
        # btn.clicked.connect(self.action_cube_left_2)
        #
        # btn = QtWidgets.QPushButton(self)
        # btn.move(750, 150)
        # btn.setText("Вправо")
        # btn.clicked.connect(self.action_cube_right_2)
        #
        # """3-я грань"""
        # btn = QtWidgets.QPushButton(self)
        # btn.move(170, 400)
        # btn.setText("Влево")
        # btn.clicked.connect(self.action_cube_left_3)
        #
        # btn = QtWidgets.QPushButton(self)
        # btn.move(370, 540)
        # btn.setText("Вправо")
        # btn.clicked.connect(self.action_cube_right_3)
        #
        # """4-я грань"""
        # btn = QtWidgets.QPushButton(self)
        # btn.move(570, 540)
        # btn.setText("Влево")
        # btn.clicked.connect(self.action_cube_left_4)
        #
        # btn = QtWidgets.QPushButton(self)
        # btn.move(750, 400)
        # btn.setText("Вправо")
        # btn.clicked.connect(self.action_cube_right_4)
        #
        # """Центр"""
        # btn = QtWidgets.QPushButton(self)
        # btn.move(50, 270)
        # btn.setText("Влево")
        # btn.clicked.connect(self.action_cube_center_left)
        #
        # btn = QtWidgets.QPushButton(self)
        # btn.move(850, 270)
        # btn.setText("Вправо")
        # btn.clicked.connect(self.action_cube_center_right)

        """full"""
        btn = QtWidgets.QPushButton(self)
        btn.move(880, 295)
        btn.setText("Собрать")
        btn.clicked.connect(self.setFullCube)
        #btn.clicked.connect(self.newGame)
        self.show()

    def updateFrame(self):
        self.update()

        #todo: забиндить кнопки ОК и CLOSE
        cube = game.cube_full
        if (game.checkWin(cube)):
            win = QtWidgets.QMessageBox()
            win.setWindowTitle("Победа")
            win.setText("Поздравляем! Вы сорбрали кубик!")

            win.setIcon(QtWidgets.QMessageBox.Icon.Information)
            win.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Close)
            win.buttonClicked.connect(self.popup_action)

            win.exec_()

    def popup_action(self, btn):
        if btn.text() == "OK":
            self.newGame()
        elif btn.text() == "Close":
            self.close()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        cube = game.cube_full
        self.drawCube(qp, cube)
        qp.end()

    def drawRectangles(self, qp):

        col = QtGui.QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QtGui.QColor(255, 0, 0)) # red
        qp.drawRect(10, 15, 100, 100)

        qp.setBrush(QtGui.QColor(255, 255, 0)) # жёлтый
        qp.drawRect(130, 15, 100, 100)


        qp.setBrush(QtGui.QColor(0, 0, 255))  # blue
        qp.drawRect(250, 15, 100, 100)
        qp.setBrush(QtGui.QColor(0, 255, 0))  # green
        qp.drawRect(370, 15, 100, 100)


    def drawCube(self, qp, cube):

        #TODO: ПОЧЕМУ ТО МАССИВ ОТРИСОВЫВАЕТСЯ В КОНСОЛЬ НЕСКОЛЬКО РАЗ ПРИ НАВЕДЕНИИ НА КНОПКУ!!!
        col = QtGui.QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        vert = 0
        hor = 0
        cube_full = cube
        # main.print_array(cube_full)

        for i in range (len(cube_full)):

            for j in range (len(cube_full[i])):

                if (cube_full[i][j] == "с"):
                    qp.setBrush(QtGui.QColor(0, 0, 255))  # blue
                    qp.drawRect(300 + vert, 100 + hor, 100, 100)
                    vert += 100
                if (cube_full[i][j] == "ж"):
                    qp.setBrush(QtGui.QColor(255, 255, 0))  # yellow
                    qp.drawRect(300 + vert, 100 + hor, 100, 100)
                    vert += 100
                if (cube_full[i][j] == "з"):
                    qp.setBrush(QtGui.QColor(0, 255, 0))  # green
                    qp.drawRect(300 + vert, 100 + hor, 100, 100)
                    vert += 100
                if (cube_full[i][j] == "к"):
                    qp.setBrush(QtGui.QColor(255, 0, 0))  # red
                    qp.drawRect(300 + vert, 100 + hor, 100, 100)
                    vert += 100
            hor += 100
            vert = 0
        game.print_array(cube_full)

    def newGame(self):
        self.close()
        import game
        game.cube_full = game.newGame()
        self.__init__()

        # todo: не работает :(
        # cube = main.cube_full
        # if (main.checkWin(cube)):
        #     self.updateFrame()
        #     win = QtWidgets.QMessageBox()
        #     win.setWindowTitle("Победа")
        #     win.setText("Поздравляем! Вы сорбрали кубик!")
        #     win.setIcon(QtWidgets.QMessageBox.Icon.Information)
        #     win.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Close)
        #     win.exec_()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

