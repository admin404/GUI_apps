import pyautogui as pag
import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

# thread


class thread(QThread):
    trig = Signal()

    def __init__(self):
        super().__init__()
        self.flag = 1

    def run(self):
        mouse_position()


# main window
class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.ui()

    def ui(self):
        self.setWindowTitle("Project Starter")
        self.setCentralWidget(main_widget())


# main widget
class main_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.position_label = QLabel()
        self.position_label.setText("")

        self.btn = QPushButton()
        self.btn.setText("Start")
        self.btn.pressed.connect(self.action_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.position_label)
        self.layout.addWidget(self.btn)

    def action_handler(self):
        sg = self.btn.text()
        if sg == "Start":
            self.thread = thread()
            self.thread.start()
            self.btn.setText("Stop")
            print(mouse_position())
            # self.position_label.setText(mouse_position)
            # print(mouse_position())

        else:
            self.btn.setText("Start")
            self.thread.terminate()


# mouse position
class mouse_position:
    def __init__(self):
        self.get_position()

    def __str__(self):
        pass

    def get_position(self):
        position = pag.position()
        x, y = pag.position()
        return x, y
        # while 1:
        # if pag.position() != position:
        # print(pag.Size(pag.position))
        # x, y = pag.position()
        # return x, y
        # print(pag.position())
        # print(type(pag.position()))
        # _ = os.system("cls")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())

# pag.moveTo(0, 0)
