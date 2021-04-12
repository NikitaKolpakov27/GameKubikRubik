import sys
from random import randint

from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtGui import QPen, QColor

import main



class Example(QtWidgets.QWidget):
    YELLOW = "ffff00"
    BLUE = "0000ff"
    GREEN = "008000"
    RED = "ff0000"

    def __init__(self):
        super().__init__()
        self.initUI()

    def action_cube_right_1(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][0]
        data1[0][1] = cube_full[0][1]
        data1[1][0] = cube_full[1][0]
        data1[1][1] = cube_full[1][1]

        data1 = main.list_rot_right(data1)
        cube_full[0][0] = data1[0][0]
        cube_full[0][1] = data1[0][1]
        cube_full[1][0] = data1[1][0]
        cube_full[1][1] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_left_1(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][0]
        data1[0][1] = cube_full[0][1]
        data1[1][0] = cube_full[1][0]
        data1[1][1] = cube_full[1][1]

        data1 = main.list_rot_left(data1)
        cube_full[0][0] = data1[0][0]
        cube_full[0][1] = data1[0][1]
        cube_full[1][0] = data1[1][0]
        cube_full[1][1] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_left_2(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][2]
        data1[0][1] = cube_full[0][3]
        data1[1][0] = cube_full[1][2]
        data1[1][1] = cube_full[1][3]

        data1 = main.list_rot_left(data1)
        cube_full[0][2] = data1[0][0]
        cube_full[0][3] = data1[0][1]
        cube_full[1][2] = data1[1][0]
        cube_full[1][3] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_right_2(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[0][2]
        data1[0][1] = cube_full[0][3]
        data1[1][0] = cube_full[1][2]
        data1[1][1] = cube_full[1][3]

        data1 = main.list_rot_right(data1)
        cube_full[0][2] = data1[0][0]
        cube_full[0][3] = data1[0][1]
        cube_full[1][2] = data1[1][0]
        cube_full[1][3] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_left_3(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][0]
        data1[0][1] = cube_full[2][1]
        data1[1][0] = cube_full[3][0]
        data1[1][1] = cube_full[3][1]

        data1 = main.list_rot_left(data1)
        cube_full[2][0] = data1[0][0]
        cube_full[2][1] = data1[0][1]
        cube_full[3][0] = data1[1][0]
        cube_full[3][1] = data1[1][1]

        main.cube_full = cube_full


    def action_cube_right_3(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][0]
        data1[0][1] = cube_full[2][1]
        data1[1][0] = cube_full[3][0]
        data1[1][1] = cube_full[3][1]

        data1 = main.list_rot_right(data1)
        cube_full[2][0] = data1[0][0]
        cube_full[2][1] = data1[0][1]
        cube_full[3][0] = data1[1][0]
        cube_full[3][1] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_right_4(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][2]
        data1[0][1] = cube_full[2][3]
        data1[1][0] = cube_full[3][2]
        data1[1][1] = cube_full[3][3]

        data1 = main.list_rot_right(data1)
        cube_full[2][2] = data1[0][0]
        cube_full[2][3] = data1[0][1]
        cube_full[3][2] = data1[1][0]
        cube_full[3][3] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_left_4(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[2][2]
        data1[0][1] = cube_full[2][3]
        data1[1][0] = cube_full[3][2]
        data1[1][1] = cube_full[3][3]

        data1 = main.list_rot_left(data1)
        cube_full[2][2] = data1[0][0]
        cube_full[2][3] = data1[0][1]
        cube_full[3][2] = data1[1][0]
        cube_full[3][3] = data1[1][1]

        main.cube_full = cube_full

    def action_cube_center_left(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[1][1]
        data1[0][1] = cube_full[1][2]
        data1[1][0] = cube_full[2][1]
        data1[1][1] = cube_full[2][2]

        data1 = main.list_rot_left(data1)
        cube_full[1][1] = data1[0][0]
        cube_full[1][2] = data1[0][1]
        cube_full[2][1] = data1[1][0]
        cube_full[2][2] = data1[1][1]

        main.cube_full = cube_full


    def action_cube_center_right(self):
        self.updateFrame()
        cube_full = main.cube_full
        data1 = [["o", "o"], ["o", "o"]]
        data1[0][0] = cube_full[1][1]
        data1[0][1] = cube_full[1][2]
        data1[1][0] = cube_full[2][1]
        data1[1][1] = cube_full[2][2]

        data1 = main.list_rot_right(data1)
        cube_full[1][1] = data1[0][0]
        cube_full[1][2] = data1[0][1]
        cube_full[2][1] = data1[1][0]
        cube_full[2][2] = data1[1][1]

        main.cube_full = cube_full


    def setFullCube(self):
        self.updateFrame()
        cube_full = main.cube_full
        cube_full = [["к", "к" ,"з" ,"з"], ["к", "к", "з", "з"], ["ж", "ж", "с", "с"], ["ж","ж" ,"с" ,"с"]]
        main.cube_full = cube_full



    def initUI(self):
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Colours')

        """1-я грань"""
        btn = QtWidgets.QPushButton(self)
        btn.move(170, 150)
        btn.setText("Влево")
        btn.clicked.connect(self.action_cube_left_1)

        btn = QtWidgets.QPushButton(self)
        btn.move(370, 40)
        btn.setText("Вправо")
        btn.clicked.connect(self.action_cube_right_1)

        """2-я грань"""
        btn = QtWidgets.QPushButton(self)
        btn.move(570, 40)
        btn.setText("Влево")
        btn.clicked.connect(self.action_cube_left_2)

        btn = QtWidgets.QPushButton(self)
        btn.move(750, 150)
        btn.setText("Вправо")
        btn.clicked.connect(self.action_cube_right_2)

        """3-я грань"""
        btn = QtWidgets.QPushButton(self)
        btn.move(170, 400)
        btn.setText("Влево")
        btn.clicked.connect(self.action_cube_left_3)

        btn = QtWidgets.QPushButton(self)
        btn.move(370, 540)
        btn.setText("Вправо")
        btn.clicked.connect(self.action_cube_right_3)

        """4-я грань"""
        btn = QtWidgets.QPushButton(self)
        btn.move(570, 540)
        btn.setText("Влево")
        btn.clicked.connect(self.action_cube_left_4)

        btn = QtWidgets.QPushButton(self)
        btn.move(750, 400)
        btn.setText("Вправо")
        btn.clicked.connect(self.action_cube_right_4)

        """Центр"""
        btn = QtWidgets.QPushButton(self)
        btn.move(50, 270)
        btn.setText("Влево")
        btn.clicked.connect(self.action_cube_center_left)

        btn = QtWidgets.QPushButton(self)
        btn.move(850, 270)
        btn.setText("Вправо")
        btn.clicked.connect(self.action_cube_center_right)

        """full"""
        btn = QtWidgets.QPushButton(self)
        btn.move(880, 295)
        btn.setText("Собрать")
        btn.clicked.connect(self.setFullCube)


        # cube = main.cube_full
        # if (main.checkWin(cube)):
        #     win = QtWidgets.QMessageBox()
        #     win.setWindowTitle("Победа")
        #     win.setText("Поздравляем! Вы сорбрали кубик!")
        #     win.setIcon(QtWidgets.QMessageBox.Icon.Information)
        #     win.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Close)
        #     win.exec_()


        self.show()

    def updateFrame(self):
        self.update()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        cube = main.cube_full
        self.drawCube(qp, cube)

        # qp.end()

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
        main.print_array(cube_full)

        if (main.checkWin(cube)):
            win = QtWidgets.QMessageBox()
            win.setWindowTitle("Победа")
            win.setText("Поздравляем! Вы сорбрали кубик!")
            win.setIcon(QtWidgets.QMessageBox.Icon.Information)
            win.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Close)

            win.exec_()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

