import sys, os
from PySide2.QtCore import QSize
from PySide2.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QPushButton
    )

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Main import Main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mandelbrot Set")
        self.setMinimumSize(QSize(400,300))
        self.setMaximumSize(QSize(1200,900)) 

        button = QPushButton("Render Image") 
        button.clicked.connect(self.call_mandelbrotset)

        self.setCentralWidget(button)

    def call_mandelbrotset (self): 
        Main.main()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_() 

    print("EXIT: Program closing")
