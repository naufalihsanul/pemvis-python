import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QTimer
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("ini aplikasi")
        self.resize(400,300)

        self.labelEmail = QLabel("Email: ")
        self.inputEmail = QLineEdit()
        self.labelPassword = QLabel("Password: ")
        self.inputPassword = QLineEdit()
        self.buttonLogin = QPushButton("Login")


        layout = QVBoxLayout()

        layout.addWidget(self.labelEmail)
        layout.addWidget(self.inputEmail)
        layout.addWidget(self.labelPassword)
        layout.addWidget(self.inputPassword)
        layout.addWidget(self.buttonLogin)


        self.buttonLogin.clicked.connect(self.cekLogin)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        self.setLayout(layout)
    
    def cekLogin(self):
        if self.inputEmail.text() == "admin" and self.inputPassword.text() == "12345678":
            self.buttonLogin.setText("Login berhasil")
        else:
            self.buttonLogin.setText("password dan email salah")
        
       
        self.inputEmail.setText("")
        self.inputPassword.setText("")

        # Kembalikan teks button ke "Login" setelah 3 detik (3000 ms)
        QTimer.singleShot(3000, lambda: self.buttonLogin.setText("Login"))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
