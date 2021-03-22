import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()


    def setup_ui(self):
        self.setCentralWidget(gui())
        self.setWindowTitle("TEST")


class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.btn = QPushButton()
        self.btn.setText("Hello")
        self.btn.clicked.connect(self.say_hello)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.btn)

    def say_hello(self):
        print("Hello")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())