import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import Qt

class KalkulatorWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.resize(400, 150)

        self.layout_utama = QVBoxLayout()
        self.layout_input = QHBoxLayout() 
        
        self.label_judul = QLabel("Aplikasi Kalkulator")
        self.label_judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_utama.addWidget(self.label_judul)

        self.input_pertama = QLineEdit()
        self.input_pertama.setPlaceholderText("Angka 1")
        
        self.combo_operasi = QComboBox()
        self.combo_operasi.addItem("+")
        self.combo_operasi.addItem("-")
        self.combo_operasi.addItem("x")
        self.combo_operasi.addItem("÷")

        self.layout_input.addWidget(self.input_pertama)
        self.layout_input.addWidget(self.combo_operasi)

        self.input_kedua = QLineEdit()
        self.input_kedua.setPlaceholderText("Angka 2")
        self.layout_input.addWidget(self.input_kedua)
        
        self.btn_hitung = QPushButton("Hitung")
        self.btn_hitung.setEnabled(False)
        self.btn_hitung.setShortcut("Return")
        
        self.layout_utama.addLayout(self.layout_input)
        self.layout_utama.addWidget(self.btn_hitung)

        self.input_pertama.textChanged.connect(self.cek_validasi)
        self.input_kedua.textChanged.connect(self.cek_validasi)

        self.btn_clear = QPushButton("Clear Data")
        self.btn_clear.setShortcut("Esc")
        self.layout_utama.addWidget(self.btn_clear)

        self.label_hasil = QLabel("Hasil: ")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_utama.addWidget(self.label_hasil)

        self.setLayout(self.layout_utama)

        self.btn_hitung.clicked.connect(self.proses_hitung)
        self.btn_clear.clicked.connect(self.bersihkan_layar)


    def proses_hitung(self):
        angka_1 = float(self.input_pertama.text())
        angka_2 = float(self.input_kedua.text())
        operasi = self.combo_operasi.currentText()

        hasil = 0

        if operasi == "+":
            hasil = angka_1 + angka_2
        elif operasi == "-":
            hasil = angka_1 - angka_2
        elif operasi == "x":
            hasil = angka_1 * angka_2
        elif operasi == "÷":
            if angka_2 == 0:
                self.label_hasil.setText("Error: Tidak bisa dibagi 0")
                return
            hasil = angka_1 / angka_2

        self.label_hasil.setText(f"Hasil: {hasil}")

    def cek_validasi(self):
        isi_teks_1 = self.input_pertama.text()
        isi_teks_2 = self.input_kedua.text()

        try:
            if isi_teks_1 != "": float(isi_teks_1)
            if isi_teks_2 != "": float(isi_teks_2)
            
            if isi_teks_1 != "" and isi_teks_2 != "":
                self.btn_hitung.setEnabled(True)
            else:
                self.btn_hitung.setEnabled(False)
                
        except ValueError:
            self.btn_hitung.setEnabled(False)

    def closeEvent(self, event):
        kotak_tanya = QMessageBox()
        kotak_tanya.setWindowTitle("Konfirmasi Keluar")
        kotak_tanya.setText("Yakin mau menutup aplikasi kalkulator ini?")
        
        tombol_yes_no = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        kotak_tanya.setStandardButtons(tombol_yes_no)

        jawaban_user = kotak_tanya.exec()

        if jawaban_user == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def bersihkan_layar(self):
        self.input_pertama.clear()
        self.input_kedua.clear()
        self.label_hasil.setText("Hasil: ")
        self.btn_hitung.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_kalkulator = KalkulatorWindows()
    window_kalkulator.show()
    sys.exit(app.exec())