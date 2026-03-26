import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class MainWindows(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("ini aplikasi")
        self.resize(500,400)

        layout = QVBoxLayout()

        inputEmail = QLineEdit()
        inputEmail.setPlaceholderText("Masukan email")

        inpurPassword = QLineEdit()
        inpurPassword.setPlaceholderText("masukan Password")

        tombolLogin = QPushButton("Login")

        layout.addWidget(inputEmail)
        layout.addWidget(inpurPassword)
        layout.addWidget(tombolLogin)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(10)
        

        self.setLayout(layout)

apk = QApplication(sys.argv)
window = MainWindows()

window.show()

sys.exit(apk.exec())





