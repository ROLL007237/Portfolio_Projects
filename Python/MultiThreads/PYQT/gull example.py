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


class BtnChanger(Thread):
	def __init__(self, comm: Communication):
		super().__init__(daemon=True)
		self.comm = comm
		self.start()

	def run(self):
		seconds = 0
		while True:
			seconds += 1
			self.comm.event_signal.emit(f"Total seconds {seconds} slept")
			sleep(1)


class ClickerCounter(Thread):
	def __init__(self):
		super().__init__(daemon=True)
		self.event = Event()
		self.counter = 0
		self.start()

	def run(self):
		while True:
			self.event.wait()
			self.counter += 1
			print('clicked!', self.counter)
			self.event.clear()


class MySuperApp(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle('example')
		self.setMinimumSize(400, 400)  # width, height

		self.counter = 0
		clicker = ClickerCounter()
		self.event = clicker.event

		self.comm = Communication()

		# example of our custom signal object
		self.btn_changer = BtnChanger(self.comm)

		btn = QPushButton("Click me!")
		btn.setMaximumSize(100, 100)
		btn.clicked.connect(self.click_me)
		self.comm.event_signal.connect(self.print_it)

		self.btn2 = QPushButton("kek")  # QLabel("Hello World!")
		self.btn2.setMaximumSize(100, 100)

		vertical_layout = QGridLayout()
		# vertical
		# horizontal
		# grid
		# forms
		vertical_layout.addWidget(btn)
		vertical_layout.addWidget(self.btn2)

		# self.setCentralWidget(btn)
		self.setLayout(vertical_layout)
		self.show()

	@pyqtSlot(str)
	def print_it(self, text: str):
		self.btn2.setText(text)

	@pyqtSlot()
	def click_me(self):
		self.event.set()
	# x, y = random.randint(0, 400), random.randint(0, 400)
	# # white/purple/
	# # rgb(100, 100, 100)
	# # 0 - 255 00-FF
	# r, g, b = [random.randint(0, 255) for _ in range(3)]
	# value = sum((r, g, b)) / 3
	# text_color = 'white' if value < 128 else 'black'
	# self.label.setStyleSheet(f"background-color: rgb({r}, {g}, {b}); color: {text_color}")


app = QApplication([])
window = MySuperApp()
app.exec()
