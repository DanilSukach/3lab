import sys
from create_csv import create_csv
from copy_random import copy_random
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QDesktopWidget,
    QLineEdit,
    QInputDialog,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn_1 = QPushButton("Создать файл анотацию исходного датасета", self)
        self.btn_1.move(50, 20)
        self.btn_1.clicked.connect(self.showDialog_1)
        self.btn_2 = QPushButton("Создание датасета с другой организацией файлов", self)
        self.btn_2.move(50, 60)
        self.btn_2.clicked.connect(self.showDialog_2)

        self.resize(1000, 400)
        self.center()
        self.setWindowTitle("lab3")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog_1(self):

        text, ok = QInputDialog.getText(self, "Input Dialog", "Введите путь к папке:")

        if ok:

            self.create_file = create_csv(str(text))

    def showDialog_2(self):

        text, ok = QInputDialog.getText(self, "Input Dialog", "Введите путь к папке:")

        if ok:

            self.create_file = copy_random(str(text))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
