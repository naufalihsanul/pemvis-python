import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QComboBox, QPushButton)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        
        # --- KONFIGURASI JENDELA (Materi 1 & 2) ---
        self.setWindowTitle("Aplikasi Form Biodata Mahasiswa")
        self.resize(400, 600)
        self.setStyleSheet("background-color: white;")

        # Layout Utama
        self.main_layout = QVBoxLayout()
        # Mengatur jarak antar baris menjadi sangat kecil (5 pixel)
        self.main_layout.setSpacing(5) 
        self.main_layout.setContentsMargins(25, 25, 25, 25)

        # --- INPUT NAMA ---
        self.label_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan Nama Lengkap")
        # Style langsung di tempat
        self.input_nama.setStyleSheet("border: 1px solid #27ae60; border-radius: 4px; padding: 7px;")
        
        self.main_layout.addWidget(self.label_nama)
        self.main_layout.addWidget(self.input_nama)

        # --- INPUT NIM (Persyaratan 1) ---
        self.label_nim = QLabel("NIM:")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        self.input_nim.setStyleSheet("border: 1px solid #27ae60; border-radius: 4px; padding: 7px;")
        
        self.main_layout.addWidget(self.label_nim)
        self.main_layout.addWidget(self.input_nim)

        # --- INPUT KELAS (Persyaratan 2) ---
        self.label_kelas = QLabel("Kelas:")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")
        self.input_kelas.setStyleSheet("border: 1px solid #27ae60; border-radius: 4px; padding: 7px;")
        
        self.main_layout.addWidget(self.label_kelas)
        self.main_layout.addWidget(self.input_kelas)

        # --- COMBOBOX JENIS KELAMIN (Persyaratan 3) ---
        self.label_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])
        self.combo_jk.setStyleSheet("border: 1px solid #ccc; border-radius: 4px; padding: 7px; background: white;")
        
        self.main_layout.addWidget(self.label_jk)
        self.main_layout.addWidget(self.combo_jk)

        # --- TOMBOL-TOMBOL (Persyaratan 4 & 5) ---
        self.h_layout_tombol = QHBoxLayout()
        
        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_tampilkan.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px; padding: 10px; font-weight: bold;")
        
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("background-color: #95a5a6; color: white; border-radius: 5px; padding: 10px; font-weight: bold;")
        
        self.h_layout_tombol.addWidget(self.btn_tampilkan)
        self.h_layout_tombol.addWidget(self.btn_reset)
        
        # Tambah sedikit jarak atas sebelum tombol
        self.main_layout.addSpacing(10)
        self.main_layout.addLayout(self.h_layout_tombol)

        # --- LABEL HASIL (Area Hijau) ---
        self.main_layout.addSpacing(15)
        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)
        # Style langsung di tempat
        self.label_hasil.setStyleSheet("background-color: #dcf2e1; border-left: 5px solid #27ae60; padding: 15px; color: #1e5631;")
        self.label_hasil.hide() # Awalnya sembunyi
        
        self.main_layout.addWidget(self.label_hasil)
        
        # Set Layout ke jendela
        self.setLayout(self.main_layout)

        # --- LOGIKA SIGNAL & SLOT (Materi 6) ---
        self.btn_tampilkan.clicked.connect(self.klik_tampilkan)
        self.btn_reset.clicked.connect(self.klik_reset)

    def klik_tampilkan(self):
        # Ambil teks
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        kelas = self.input_kelas.text()
        jk = self.combo_jk.currentText()

        # Validasi (Persyaratan 6): Semua field harus diisi
        if nama == "" or nim == "" or kelas == "":
            self.label_hasil.setText("<b>Peringatan:</b> Semua field wajib diisi!")
            self.label_hasil.setStyleSheet("background-color: #fce4e4; border-left: 5px solid #e74c3c; padding: 15px; color: #c0392b;")
            self.label_hasil.show()
        else:
            # Tampilkan semua data di label hasil
            hasil = (f"<b>DATA BIODATA</b><br><br>"
                     f"Nama: {nama}<br>"
                     f"NIM: {nim}<br>"
                     f"Kelas: {kelas}<br>"
                     f"Jenis Kelamin: {jk}")
            self.label_hasil.setText(hasil)
            self.label_hasil.setStyleSheet("background-color: #dcf2e1; border-left: 5px solid #27ae60; padding: 15px; color: #1e5631;")
            self.label_hasil.show()

    def klik_reset(self):
        # Mengosongkan semua input (Persyaratan 5)
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.label_hasil.hide()

# --- RUN PROGRAM (Cara 3 Materi 1) ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())