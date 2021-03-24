import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.setWindowTitle("Project Starter")
        self.resize(242, 100)

    def set_ui(self):
        types = ["Django", "PySide"]

        self.project_type = QComboBox()
        for projectType in types:
            self.project_type.addItem(projectType)

        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.project_type)
        self.layout.addWidget(self.submit)

    def submit_handler(self):
        project_type_id = self.project_type.currentIndex()
        print(project_type_id)
        self.project_type.setHidden(1)
        self.submit.setHidden(1)
        if project_type_id == 0:
            self.close()
            self.django_choose_action = django_action_chose()
            self.django_choose_action.show()
        if project_type_id == 1 or project_type_id == 2:
            self.close()
            self.pyside_choose_action = pyside_action_choose()
            self.pyside_choose_action.show()


class django_action_chose(QWidget):
    def __init__(self):
        super().__init__()
        self.django_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def django_ui(self):
        actions = [
            "start django app",
            "Start Django Server",
            "make migrations for django",
        ]

        self.action = QComboBox()
        for action in actions:
            self.action.addItem(action)

        self.submit_action = QPushButton()
        self.submit_action.setText("Submit")

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_action)

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.action)
        self.layout.addWidget(self.submit_action)
        self.layout.addWidget(self.back)

    def back_action(self):
        self.close()
        self.main_ui = main()
        self.main_ui.show()


class pyside_action_choose(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside_ui(self):
        actions = [
            "Install PySide2",
            "Install PySide6",
            "Start PySide2 app",
            "Start PySide6 app",
        ]

        self.action = QComboBox()
        for action in actions:
            self.action.addItem(action)

        self.submit_action = QPushButton()
        self.submit_action.setText("Submit")

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_action)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.action)
        self.layout.addWidget(self.submit_action)
        self.layout.addWidget(self.back)

    def back_action(self):
        self.close()
        self.main_ui = main()
        self.main_ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
