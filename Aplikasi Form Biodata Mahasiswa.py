import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class mainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Aplikasi Form Biodata Mahasiswa")
        self.resize(450, 550)

        layout = QVBoxLayout()
        layout.setSpacing(5)

        labelNama = QLabel("Nama Lengkap:")
        self.inputNama = QLineEdit()
        self.inputNama.setPlaceholderText("Budi Santoso")

        labelNIM = QLabel("NIM:")
        self.inputNIM = QLineEdit()
        self.inputNIM.setPlaceholderText("Masukkan NIM")

        labelKelas = QLabel("Kelas:")
        self.inputKelas = QLineEdit()
        self.inputKelas.setPlaceholderText("Contoh: TI-2A")

        labelJK = QLabel("Jenis Kelamin:")
        self.comboJK = QComboBox()
        self.comboJK.addItems(["Laki-laki", "Perempuan"])

        layout.addWidget(labelNama)
        layout.addWidget(self.inputNama)
        layout.addWidget(labelNIM)
        layout.addWidget(self.inputNIM)
        layout.addWidget(labelKelas)
        layout.addWidget(self.inputKelas)
        layout.addWidget(labelJK)
        layout.addWidget(self.comboJK)

        layoutTombol = QHBoxLayout()
        self.btnTampilkan = QPushButton("Tampilkan")
        self.btnReset = QPushButton("Reset")
        
        layoutTombol.addWidget(self.btnTampilkan)
        layoutTombol.addWidget(self.btnReset)
        layout.addLayout(layoutTombol)

        self.labelHasil = QLabel("")
        self.labelHasil.setStyleSheet("background-color: #dcf2e1; border-left: 5px solid #27ae60; padding: 10px;")
        self.labelHasil.setVisible(False)
        layout.addWidget(self.labelHasil)

        self.btnTampilkan.clicked.connect(self.tampilkan_data)
        self.btnReset.clicked.connect(self.reset_data)

        self.setLayout(layout)

    def tampilkan_data(self):
        nama = self.inputNama.text()
        nim = self.inputNIM.text()
        kelas = self.inputKelas.text()
        jk = self.comboJK.currentText()

        if not nama or not nim or not kelas:
            self.labelHasil.setText("Semua field harus diisi")
            self.labelHasil.setStyleSheet("background-color: #fce4e4; border-left: 5px solid #e74c3c; padding: 10px;")
            self.labelHasil.setVisible(True)
        else:
            hasil = f"Nama: {nama}\nNIM: {nim}\nKelas: {kelas}\nJenis Kelamin: {jk}"
            self.labelHasil.setText(hasil)
            self.labelHasil.setStyleSheet("background-color: #dcf2e1; border-left: 5px solid #27ae60; padding: 10px;")
            self.labelHasil.setVisible(True)

    def reset_data(self):
        self.inputNama.clear()
        self.inputNIM.clear()
        self.inputKelas.clear()
        self.comboJK.setCurrentIndex(0)
        self.labelHasil.setVisible(False)

app = QApplication(sys.argv)
window = mainWindows()
window.show()

sys.exit(app.exec())