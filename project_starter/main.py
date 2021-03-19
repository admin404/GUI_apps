import pyautogui
import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class mouse_position():
    def __init__(self):
        self.get_position()

    def get_position(self):
        position = pyautogui.position()
        while 1:
            if (pyautogui.position() != position):
                print(pyautogui.position())
                self.clear()

    def clear(self):
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setWindowTitle("Project Starter")
        self.setCentralWidget(widget())


class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.action_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.submit)

    def action_handler(self):
        mouse_position()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())