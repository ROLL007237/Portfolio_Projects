from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout
)

class MySuperApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ARBUZ')
        self.setMinimumSize(400, 400)  # width, height

        btn1 = QPushButton("Click me 1!")
        btn1.setMaximumSize(100, 50)
        btn1.clicked.connect(lambda: self.btn_click('1'))

        btn2 = QPushButton("Click me 2!")
        btn2.setMaximumSize(100, 50)
        btn2.clicked.connect(lambda: self.btn_click('2'))

        btn3 = QPushButton("Click me 3!")
        btn3.setMaximumSize(100, 50)
        btn3.clicked.connect(lambda: self.btn_click('3'))

        vertical_layout = QGridLayout()
        vertical_layout.addWidget(btn1)
        vertical_layout.addWidget(btn2)
        vertical_layout.addWidget(btn3)

        self.setLayout(vertical_layout)
        self.show()

    def btn_click(self,arg):
        print(arg)


app = QApplication([])
window = MySuperApp()
app.exec()
