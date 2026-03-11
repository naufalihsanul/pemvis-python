import sys

from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel, QLineEdit,QComboBox

class mainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Biodata rendy moy")
        self.resize(500,300)

        layout = QVBoxLayout()

        labelNama = QLabel("Nama Lengkap:")
        inputNama = QLineEdit()
        inputNama.setPlaceholderText("Budi santoso")

        labelNIM = QLabel("NIM:")
        inputNIM = QLineEdit()
        inputNIM.setPlaceholderText("F1D02310084")

        labelKelas = QLabel("Kelas:")
        inputKelas = QLineEdit()
        inputKelas.setPlaceholderText("TI-2A")
        
        layout.addWidget(labelNama)
        layout.addWidget(inputNama)

        layout.addWidget(labelNIM)
        layout.addWidget(inputNIM)

        layout.addWidget(labelKelas)
        layout.addWidget(inputKelas)

        # ini combo box nya bro

        combo = QComboBox()
        combo.addItems(["Laki-Laki", "Perempuan"])

        labelCombo = QLabel("Jenis-Kelamin")

        layout.addWidget(labelCombo)
        layout.addWidget(combo)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = mainWindows()
window.show()

sys.exit(app.exec())