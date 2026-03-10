import sys

from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLabel

class coba(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    
    def setup_ui(self):
        self.setWindowTitle("ini aplikasi")

        layout = QVBoxLayout()

        label = QLabel("ini label")
        tombol = QPushButton("ini tombol saya")

        layout.addWidget(label)
        layout.addWidget(tombol)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = coba()
window.show()

sys.exit(app.exec())