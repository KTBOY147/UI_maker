from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("You pressed the butt")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Subodh")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Abe beee!!!")
        self.b1.clicked.connect(self.button_clicked)

    def update(self): 
        self.label.adjustSize()
        self.label.setStyleSheet("background-color:cyan")
    


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()