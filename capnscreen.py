# Screen capture by tlil 01/04/2020
from mss import mss

from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox

app = QApplication([])
button = QPushButton('Capture')

def on_button_click():
    alert = QMessageBox()
    alert.setText("Screen captured")
    alert.exec_()
    with mss() as sct:
        sct.shot()
    
button.clicked.connect(on_button_click)  # connect signal clicked with method
button.show()
app.exec_()
