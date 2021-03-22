import pyautogui
import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

# main thread
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
        self.setCentralWidget(widget())

# main Widget
class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.btn = QPushButton()
        self.btn.setText("Start")
        self.btn.pressed.connect(self.action_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.btn)

    def action_handler(self):
        sg = self.btn.text()
        if sg == 'Start':
        	self.thread = thread()
        	self.thread.start()
        	self.btn.setText('Stop')

        else:
        	self.btn.setText('Start')
        	self.thread.terminate()

# mouse position function
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())