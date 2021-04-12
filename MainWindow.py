from PyQt5 import Qt


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.scene = Qt.QGraphicsScene()

        self.graphics_view = Qt.QGraphicsView()
        self.graphics_view.setScene(self.scene)

        self.setCentralWidget(self.graphics_view)

    def plot(self):
        rect = Qt.QRectF(0, 0, 90, 90)
        color = Qt.Qt.green

        self.scene.addEllipse(rect, Qt.QPen(color), Qt.QBrush(color))


if __name__ == '__main__':
    app = Qt.QApplication([])

    mw = MainWindow()
    mw.show()

    mw.plot()

    app.exec()