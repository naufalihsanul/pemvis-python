# 🔄 Cheatsheet: Web → PySide6 (Python)

---

## 📦 HTML → PySide6 Widgets

| HTML | PySide6 |
|:-----|:--------|
| `<div>` | `QWidget()` |
| `<p>`, `<h1>`, `<span>` | `QLabel("teks")` |
| `<button>` | `QPushButton("teks")` |
| `<input type="text">` | `QLineEdit()` |
| `<input type="password">` | `QLineEdit()` + `.setEchoMode(QLineEdit.Password)` |
| `<input type="number">` | `QSpinBox()` |
| `<input type="checkbox">` | `QCheckBox("teks")` |
| `<input type="radio">` | `QRadioButton("teks")` |
| `<textarea>` | `QTextEdit()` |
| `<select>` | `QComboBox()` + `.addItem("opsi")` |
| `<img>` | `QLabel()` + `.setPixmap(QPixmap("path"))` |
| `<progress>` | `QProgressBar()` |
| `<table>` | `QTableWidget(rows, cols)` |
| `<section>` | `QGroupBox("Judul")` |
| Tab Panel | `QTabWidget()` |

---

## 🎨 Layout

| CSS | PySide6 | Default |
|:----|:--------|:--------|
| `flex-direction: column` | `QVBoxLayout()` | Mirip space-around (stretch) |
| `flex-direction: row` | `QHBoxLayout()` | Mirip space-around (stretch) |
| `display: grid` | `QGridLayout()` | Merata |

### ⚠️ Layout default BUKAN flex-start. Pakai `setAlignment` untuk ubah:
```python
from PySide6.QtCore import Qt  # WAJIB import ini dulu

layout.setAlignment(Qt.AlignTop)                    # Nempel atas
layout.setAlignment(Qt.AlignCenter)                 # Tengah
layout.setAlignment(Qt.AlignTop | Qt.AlignRight)    # Pojok kanan atas
```

| CSS | PySide6 |
|:----|:--------|
| `gap: 10px` | `layout.setSpacing(10)` |
| `margin` | `layout.setContentsMargins(kiri, atas, kanan, bawah)` |
| `flex: 1` | `layout.addWidget(widget, stretch=1)` |
| `space-between` | `layout.addStretch()` di antara widget |

---

## 📐 Box Model & Styling

| CSS | Via Python | Via CSS File (.css) |
|:----|:-----------|:-------------|
| `width` | `.setFixedWidth(300)` | ❌ |
| `height` | `.setFixedHeight(200)` | ❌ |
| `padding` | — | `padding: 10px;` ✅ |
| `margin` | `layout.setContentsMargins()` | `margin: 10px;` ✅ |
| `border` | — | `border: 1px solid #ccc;` ✅ |
| `border-radius` | — | `border-radius: 8px;` ✅ |
| `color` | — | `color: red;` ✅ |
| `background-color` | — | `background-color: #333;` ✅ |
| `font-size` | — | `font-size: 16px;` ✅ |
| `font-weight` | — | `font-weight: bold;` ✅ |

### 3 Cara Pasang CSS:
```python
# ① Inline (per widget)
tombol.setStyleSheet("background-color: red; color: white;")

# ② Internal (seluruh app)
app.setStyleSheet("QPushButton { background-color: blue; }")

# ③ External file (rekomendasi)
with open("style.css", "r") as f:
    app.setStyleSheet(f.read())
```

### Selector di file CSS:
```css
QPushButton { }                       /* Semua tombol */
#myId { }                             /* widget.setObjectName("myId") */
QPushButton[class="bahaya"] { }       /* widget.setProperty("class", "bahaya") */
QPushButton:hover { }
QPushButton:disabled { }
```

---

## ⚡ Event Listener — Contoh LENGKAP (Tinggal Copy-Paste & Ganti)

### Contoh: Klik Tombol + Ambil Input + Ubah Label
```python
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Contoh Event")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Belum ada nama")
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ketik nama...")

        self.tombol = QPushButton("Submit")
        self.tombol.clicked.connect(self.tombol_diklik)     # ← EVENT LISTENER

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.tombol)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    # Fungsi yang dipanggil saat tombol diklik
    def tombol_diklik(self):
        nama = self.input.text()            # Ambil value input
        if nama == "":
            self.label.setText("Nama kosong!")
            return
        self.label.setText("Halo, " + nama + "!")
        self.input.clear()                  # Kosongkan input

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

### Cara Ganti Event (Tinggal Ganti `.clicked` sesuai tabel):

| Mau apa | Ganti baris connect jadi |
|:--------|:-------------------------|
| Klik tombol | `tombol.clicked.connect(self.fungsi)` |
| Ketik di input (realtime) | `self.input.textChanged.connect(self.fungsi)` |
| Tekan Enter di input | `self.input.returnPressed.connect(self.fungsi)` |
| Pilih dropdown | `combo.currentTextChanged.connect(self.fungsi)` |
| Centang checkbox | `cek.stateChanged.connect(self.fungsi)` |
| Geser slider | `slider.valueChanged.connect(self.fungsi)` |

### Cara Ambil Value:
```python
nama = self.input.text()                # QLineEdit
teks = self.textarea.toPlainText()      # QTextEdit
checked = self.cek.isChecked()          # QCheckBox → True/False
kota = self.combo.currentText()         # QComboBox → "Jakarta"
nilai = self.slider.value()             # QSlider → angka
```

### Popup:
```python
from PySide6.QtWidgets import QMessageBox

# alert()
QMessageBox.information(self, "Info", "Data tersimpan!")

# confirm()
jawab = QMessageBox.question(self, "Konfirmasi", "Yakin hapus?")
if jawab == QMessageBox.Yes:
    print("User pilih Ya")
```

### Timer:
```python
from PySide6.QtCore import QTimer

# setInterval (berulang)
self.timer = QTimer()
self.timer.timeout.connect(self.fungsi_tiap_detik)
self.timer.start(1000)     # 1000ms = 1 detik
self.timer.stop()          # clearInterval

# setTimeout (sekali)
QTimer.singleShot(3000, self.fungsi)   # 3 detik
```

---

## 🧩 HTML Attributes → PySide6

| HTML | PySide6 |
|:-----|:--------|
| `id="..."` | `.setObjectName("...")` |
| `class="..."` | `.setProperty("class", "...")` |
| `placeholder` | `.setPlaceholderText("...")` |
| `disabled` | `.setEnabled(False)` |
| `hidden` / `display:none` | `.hide()` / `.show()` |
| `readonly` | `.setReadOnly(True)` |
| `value="..."` (set) | `.setText("...")` |
| `el.value` (get) | `.text()` |
| `checked` | `.setChecked(True)` |
| `min/max` | `.setRange(0, 100)` |
| `style="..."` | `.setStyleSheet("...")` |

---

## 🗂️ Pindah Halaman
```python
self.stack = QStackedWidget()
self.stack.addWidget(halaman1)        # index 0
self.stack.addWidget(halaman2)        # index 1
self.stack.setCurrentIndex(1)         # Pindah ke halaman 2
```

---

## 🔧 Java → Python

| Java | Python |
|:-----|:-------|
| `new Foo()` | `Foo()` |
| `this` | `self` |
| `public Foo() {}` | `def __init__(self):` |
| `super()` | `super().__init__()` |
| `null` / `true` / `false` | `None` / `True` / `False` |
| `System.out.println()` | `print()` |
| `String x = "A"` | `x = "A"` |
| `public static void main` | `if __name__ == "__main__":` |
| `;` dan `{ }` | ❌ Pakai indentasi 4 spasi |
