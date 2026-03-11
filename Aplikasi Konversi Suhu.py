import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class mainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Tugas 2 - Konversi Suhu")
        self.resize(450, 400)
        self.setStyleSheet("background-color: #f8f9fa;")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        header = QLabel("KONVERSI SUHU")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("background-color: #3498db; color: white; padding: 15px; font-weight: bold; font-size: 18px; border-radius: 5px;")
        layout.addWidget(header)

        labelInput = QLabel("Masukkan Suhu (Celsius):")
        layout.addWidget(labelInput)

        self.inputSuhu = QLineEdit()
        self.inputSuhu.setPlaceholderText("0")
        self.inputSuhu.setStyleSheet("border: 1px solid #27ae60; border-radius: 5px; padding: 10px; background-color: #f0fdf4; font-size: 16px;")
        layout.addWidget(self.inputSuhu)

        layoutTombol = QHBoxLayout()
        self.btnF = QPushButton("Fahrenheit")
        self.btnK = QPushButton("Kelvin")
        self.btnR = QPushButton("Reamur")

        styleTombol = "background-color: #3498db; color: white; padding: 12px; border-radius: 5px; font-weight: bold;"
        self.btnF.setStyleSheet(styleTombol)
        self.btnK.setStyleSheet(styleTombol)
        self.btnR.setStyleSheet(styleTombol)

        layoutTombol.addWidget(self.btnF)
        layoutTombol.addWidget(self.btnK)
        layoutTombol.addWidget(self.btnR)
        layout.addLayout(layoutTombol)

        self.labelHasil = QLabel("")
        self.labelHasil.setStyleSheet("background-color: #dbeafe; border-left: 5px solid #1e40af; padding: 20px; color: #1e40af; font-size: 14px;")
        self.labelHasil.setVisible(False)
        layout.addWidget(self.labelHasil)

        self.btnF.clicked.connect(self.ke_fahrenheit)
        self.btnK.clicked.connect(self.ke_kelvin)
        self.btnR.clicked.connect(self.ke_reamur)

        self.setLayout(layout)

    def ke_fahrenheit(self):
        try:
            celsius = float(self.inputSuhu.text())
            hasil = (celsius * 9/5) + 32
            self.tampilkan_hasil(f"{celsius} Celsius = {hasil:.2f} Fahrenheit")
        except ValueError:
            self.tampilkan_error()

    def ke_kelvin(self):
        try:
            celsius = float(self.inputSuhu.text())
            hasil = celsius + 273.15
            self.tampilkan_hasil(f"{celsius} Celsius = {hasil:.2f} Kelvin")
        except ValueError:
            self.tampilkan_error()

    def ke_reamur(self):
        try:
            celsius = float(self.inputSuhu.text())
            hasil = celsius * 4/5
            self.tampilkan_hasil(f"{celsius} Celsius = {hasil:.2f} Reamur")
        except ValueError:
            self.tampilkan_error()

    def tampilkan_hasil(self, teks):
        self.labelHasil.setText(f"<b>Hasil Konversi:</b><br><br>{teks}")
        self.labelHasil.setStyleSheet("background-color: #dbeafe; border-left: 5px solid #1e40af; padding: 20px; color: #1e40af;")
        self.labelHasil.setVisible(True)

    def tampilkan_error(self):
        self.labelHasil.setText("<b>Error:</b> Input harus berupa angka!")
        self.labelHasil.setStyleSheet("background-color: #fee2e2; border-left: 5px solid #dc2626; padding: 20px; color: #dc2626;")
        self.labelHasil.setVisible(True)

app = QApplication(sys.argv)
window = mainWindows()
window.show()
sys.exit(app.exec())