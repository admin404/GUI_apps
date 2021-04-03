import speech_recognition as sr
import pyttsx3
import sys
import os

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class thread(QThread):
    trig = Signal()

    def __init__(self):
        super().__init__()
        self.flag = 1

    def run(self):
        Voice_Recognizer()


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Recognizer")
        self.resize(260, 100)
        self.set_ui()

    def set_ui(self):
        self.text = QLabel()
        self.text.setText("")

        self.trigger = QPushButton()
        self.trigger.setText("Start")
        self.trigger.clicked.connect(self.recognize)

        self.exit = QPushButton()
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.exit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.trigger)
        self.layout.addWidget(self.exit)

    def recognize(self):
        sg = self.trigger.text()
        if sg == "Start":
            self.thread = thread()
            self.thread.start()
            self.trigger.setText("Stop")
        else:
            self.trigger.setText("Start")
            self.thread.terminate()

    def exit_handler(self):
        sys.exit()


class Voice_Recognizer:
    def __init__(self):
        self.recognize()

    def recognize(self):
        recognizer = sr.Recognizer()
        while 1:
            try:
                with sr.Microphone() as mic:
                    print("Recording ...")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio).lower()
                    print(f"{text}")
            except:
                recognizer = sr.Recognizer()
                continue


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
