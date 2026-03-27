import sys

from PySide6.QtWidgets import QApplication, QLabel, QPushButton,QLineEdit,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MainWindow (QWidget):


    def __init__(self):
        super().__init__()
        self.setup_ui()
        

    def setup_ui(self):
        self.setWindowTitle("nyoba")
        self.resize(400,300)

        self.labelEmail = QLabel("Email: ")
        self.inputEmail: QLineEdit = QLineEdit()
        
        self.labelPassword = QLabel("Password: ")
        self.inputPassword: QLineEdit = QLineEdit()
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.buttonLogin: QPushButton = QPushButton("Login")

        layout = QVBoxLayout()
        layoutCenter = QVBoxLayout()

        self.buttonLogin.clicked.connect(self.cekNama)

        
        layout.addWidget(self.labelEmail)
        layout.addWidget(self.inputEmail)
        layout.addWidget(self.labelPassword)
        layout.addWidget(self.inputPassword)
        layout.addWidget(self.buttonLogin)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layoutCenter.addLayout(layout)

        layoutCenter.setAlignment(Qt.AlignTop)

        self.setLayout(layoutCenter)

    def cekNama(self):
        if self.inputEmail.text() == "admin" and self.inputPassword.text() == "123456":
            self.buttonLogin.setText("Login berhasil")
        else:
            self.buttonLogin.setText("email atau password salah")

app  = QApplication(sys.argv)
window = MainWindow()

window.show()

sys.exit(app.exec())


        
        
    