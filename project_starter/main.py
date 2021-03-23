import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setCentralWidget(ui())


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
