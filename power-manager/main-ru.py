import os
import sys
import subprocess

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("Менеджер Питания V2.0")
        self.setFixedSize(310, 130)
        self.setCentralWidget(ui())


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.shutdown = QPushButton()
        self.shutdown.setText("Выключение")
        self.shutdown.clicked.connect(self.shutdown_handler)

        self.restart = QPushButton()
        self.restart.setText("Перезагрузка")
        self.restart.clicked.connect(self.restart_handler)

        self.sleep = QPushButton()
        self.sleep.setText("Сон")
        self.sleep.clicked.connect(self.sleep_handler)

        self.lock = QPushButton()
        self.lock.setText("Заблокировать")
        self.lock.clicked.connect(self.lock_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.shutdown)
        self.layout.addWidget(self.restart)
        self.layout.addWidget(self.sleep)
        self.layout.addWidget(self.lock)

    def shutdown_handler(self):
        print("shutdown")
        proc = subprocess.Popen(
            ["start", "cmd", "/k", "shutdown -s -f -t 00"], shell=True
        )
        proc.wait()

    def restart_handler(self):
        print("restart")
        proc = subprocess.Popen(
            ["start", "cmd", "/k", "shutdown -r -f -t 00"], shell=True
        )
        proc.wait()

    def sleep_handler(self):
        print("sleep")
        proc = subprocess.Popen(
            ["start", "cmd", "/k", "shutdown -h -f -t 00"], shell=True
        )
        proc.wait()

    def lock_handler(self):
        print("lock")
        proc = subprocess.Popen(["start", "cmd", "/k", "shutdown -l"], shell=True)
        proc.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
