import sys
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton
from PySide6.QtCore import Qt

class MainWindows(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("coba ")

        layout = QVBoxLayout()
        self.label = QLabel("blom di klik")

        self.tombol = QPushButton("klik saya")
        self.tombol.clicked.connect(self.klikTombol)

        layout.addWidget(self.label)
        layout.addWidget(self.tombol)

        

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    
    def klikTombol(self):
        self.tombol.setText("udah di klik")
        self.label.setText("hahahahahahah")

app = QApplication(sys.argv)

window = MainWindows()
window.show()

sys.exit(app.exec())