import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

import game
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QLabel

from Rules import Rules
from view import Example


class Greetings(QMainWindow):

    def __init__(self):
        super(Greetings, self).__init__()
        self.setWindowTitle("Игра \"Двумерный кубик Рубика\"")
        self.setGeometry(300, 300, 600, 600)

        self.label = QLabel(self)
        self.label.setFont(QFont('Courier New', 15))
        self.label.setText("Игра \"Двумерный кубик Рубика\"")
        self.label.adjustSize()
        self.label.move(120, 200)

        self.btn_game = QPushButton(self)
        self.btn_game.move(200, 300)
        self.btn_game.setText("Начать игру")
        self.btn_game.clicked.connect(self.show_game)
        self.btn_game.clicked.connect(self.close)

        self.btn_rules = QPushButton(self)
        self.btn_rules.move(300, 300)
        self.btn_rules.setText("Правила игры")
        self.btn_rules.clicked.connect(self.show_rules)
        self.btn_rules.clicked.connect(self.close)
        self.show()


    def show_game(self):
        self.game = Example()
        self.game.show()

    def show_rules(self):
        self.rules = Rules()
        self.rules.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Greetings()
    sys.exit(app.exec_())
