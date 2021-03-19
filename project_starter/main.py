import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setCentralWidget(widget())


class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.btn = QPushButton()
        self.btn.setText("Hello World")

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
