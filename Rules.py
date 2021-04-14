from view import Example
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFrame


class Rules(QWidget):
    def __init__(self):
        super(Rules, self).__init__()
        text = QLabel('Arial font', self)
        text.setFont(QFont('Arial', 12))
        text.setText("1. Вращайте грани кубика до тех пор, пока кубик не будет собран.\n2. Собранным кубик считается, если каждая клетка всех граней будет одного цвета.\n"
                     "3. Грани вращаются по нажатию кнопок мыши\n    3.1. Чтобы повернуть грань влево, наведите курсор на части грани и нажмите ЛКМ\n"
                     "    3.2. Чтобы повернуть грань вправо, наведите курсор на части грани и нажмите ПКМ")

        text.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.setWindowTitle('Правила игры')
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.ok = QPushButton(self)
        self.ok.move(400, 500)
        self.ok.setText("Ясно")
        self.ok.clicked.connect(self.show_game)
        self.ok.clicked.connect(self.close)

        self.show()

    def show_game(self):
        self.game = Example()
        self.game.show()