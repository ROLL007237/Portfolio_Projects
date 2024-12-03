import random
from threading import Thread, Event
from time import sleep

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QLabel, QGridLayout
)
from PyQt6.QtCore import pyqtSignal, pyqtSlot, QObject


class Communication(QObject):
    event_signal = pyqtSignal(str)


class BtnChanger(Thread()):
    def __init__(self):
        super().__init__(daemon=True)
        self.start()

    def run(self):
        seconds = 0
        while True:
            seconds += 1
            self.comm.event_signal.emit(f"Total seconds {seconds} slept")
            sleep(1)
