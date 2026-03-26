# 🌐 Cheatsheet Web: HTML + CSS + JS

---

# 🏗️ HTML

## Struktur Dasar
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Judul</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Judul</h1>
    <p>Paragraf</p>

    <script src="script.js"></script>
</body>
</html>
```

## Tag Umum
| Tag | Fungsi |
|:----|:-------|
| `<div>` | Kontainer (buat layout) |
| `<h1>`–`<h6>` | Judul |
| `<p>` | Paragraf |
| `<span>` | Teks inline (buat styling) |
| `<a href="url">` | Link |
| `<img src="foto.jpg" alt="...">` | Gambar |
| `<button>` | Tombol |
| `<ul><li>` | List |
| `<table><thead><tbody><tr><th><td>` | Tabel |

## Form
```html
<form onsubmit="return cekForm()">
    <input type="text" id="nama" placeholder="Nama" required>
    <input type="email" id="email" placeholder="Email" required>
    <input type="password" id="password" minlength="6" required>
    <input type="number" id="umur" min="1" max="100">
    <textarea id="pesan" rows="4"></textarea>

    <select id="kota">
        <option value="">Pilih</option>
        <option value="jakarta">Jakarta</option>
    </select>

    <input type="radio" name="gender" value="pria"> Pria
    <input type="radio" name="gender" value="wanita"> Wanita
    <input type="checkbox" id="setuju"> Setuju

    <button type="submit">Kirim</button>
</form>
```

---

# 🎨 CSS

## Selector
| Selector | Contoh |
|:---------|:-------|
| `tag` | `p { }` |
| `.class` | `.card { }` |
| `#id` | `#header { }` |
| `parent child` | `.nav a { }` |
| `:hover` | `button:hover { }` |
| `:focus` | `input:focus { }` |

## Flexbox
```css
.container {
    display: flex;
    flex-direction: column;       /* column = ↓, row = → (default) */
    justify-content: center;      /* Sumbu utama */
    align-items: center;          /* Sumbu silang */
    gap: 10px;
    flex-wrap: wrap;
}
```
| justify-content | Efek |
|:----------------|:-----|
| `flex-start` | Nempel awal **(default)** |
| `center` | Tengah |
| `flex-end` | Nempel akhir |
| `space-between` | Rata, pinggir nempel tepi |
| `space-around` | Jarak kiri-kanan tiap item sama |
| `space-evenly` | Semua jarak sama rata |

| align-items | Efek |
|:------------|:-----|
| `stretch` | Mengisi penuh **(default)** |
| `flex-start` | Nempel atas |
| `center` | Tengah |
| `flex-end` | Nempel bawah |

```css
/* Centering sempurna */
.center { display: flex; justify-content: center; align-items: center; height: 100vh; }

/* Anak flex ambil porsi */
.item { flex: 1; }
```

## Grid
```css
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);                         /* 3 kolom */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));  /* responsive */
    gap: 16px;
}
.item-lebar { grid-column: span 2; }
```

## Box Model
```css
* { box-sizing: border-box; margin: 0; padding: 0; }

.box {
    width: 300px;
    height: 200px;
    padding: 10px;                              /* Jarak DALAM */
    margin: 10px;                               /* Jarak LUAR */
    margin: 0 auto;                             /* Centering horizontal */
    border: 1px solid #ccc;
    border-radius: 8px;                         /* Sudut melengkung */
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);     /* Bayangan */
}
```

## Typography & Warna
```css
.teks {
    font-family: 'Segoe UI', sans-serif;
    font-size: 16px;
    font-weight: bold;
    text-align: center;           /* left, center, right */
    color: #333;
}
/* Warna: red | #ff5733 | rgba(0,0,0,0.5) */
/* Gradient: background: linear-gradient(to right, #667eea, #764ba2); */
```

## Display & Position
```css
display: none;             /* Hilang total */
display: block;            /* Tampil */
display: flex;             /* Flexbox */
display: grid;             /* Grid */
opacity: 0.5;              /* Transparan */

position: relative;        /* Relatif (bisa pakai top/left) */
position: absolute;        /* Relatif dari parent yang relative */
position: fixed;           /* Tetap di layar */
position: sticky;          /* Nempel saat scroll */
z-index: 100;

overflow: hidden;          /* Potong yang keluar */
overflow: auto;            /* Scrollbar kalau perlu */
```

## Transition & Hover
```css
.tombol {
    transition: all 0.3s ease;
}
.tombol:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
```

## Responsive
```css
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
```

---

# ⚡ JavaScript

## Ambil & Ubah Elemen
```javascript
const el = document.getElementById("judul");
const el = document.querySelector(".card");

el.textContent = "Teks baru";
el.innerHTML = "<b>Bold</b>";
el.style.color = "red";
el.style.display = "none";
el.classList.add("active");
el.classList.remove("active");
el.classList.toggle("active");
```

## Ambil Value Input
```javascript
const nama = document.getElementById("nama").value;           // input text
const pesan = document.getElementById("pesan").value;         // textarea
const kota = document.getElementById("kota").value;           // select
const setuju = document.getElementById("setuju").checked;     // checkbox (true/false)
```

## Event Listener — Contoh Lengkap

### Contoh 1: Klik Tombol
```html
<button id="tombolSaya">Klik Saya</button>
<p id="hasil"></p>

<script>
    const tombol = document.getElementById("tombolSaya");
    const hasil = document.getElementById("hasil");

    tombol.addEventListener("click", function() {
        hasil.textContent = "Tombol sudah diklik!";
    });
</script>
```

### Contoh 2: Validasi Form (onsubmit)
```html
<form onsubmit="return cekForm()">
    <input type="text" id="nama" placeholder="Nama">
    <input type="email" id="email" placeholder="Email">
    <p id="error" style="color:red"></p>
    <button type="submit">Kirim</button>
</form>

<script>
    function cekForm() {
        const nama = document.getElementById("nama").value;
        const email = document.getElementById("email").value;
        const error = document.getElementById("error");

        if (nama === "") {
            error.textContent = "Nama wajib diisi!";
            return false;      // Form TIDAK dikirim
        }
        if (!email.includes("@")) {
            error.textContent = "Email tidak valid!";
            return false;
        }

        alert("Form valid! Data siap dikirim.");
        return true;           // Form dikirim ke action/PHP
    }
</script>
```

### Contoh 3: Realtime Input
```html
<input type="text" id="cari" placeholder="Ketik sesuatu...">
<p id="preview"></p>

<script>
    const input = document.getElementById("cari");
    const preview = document.getElementById("preview");

    input.addEventListener("input", function(e) {
        preview.textContent = "Kamu ketik: " + e.target.value;
    });
</script>
```

### Daftar Event yang Sering Dipakai:
| Event | Kapan |
|:------|:------|
| `click` | Diklik |
| `input` | Input berubah (realtime) |
| `change` | Select/checkbox berubah |
| `submit` | Form disubmit |
| `keydown` | Tombol keyboard ditekan |
| `DOMContentLoaded` | Halaman selesai dimuat |

## Array (Simpan Data Sementara)
```javascript
// Buat array kosong
let daftarNama = [];

// Tambah
daftarNama.push("Budi");
daftarNama.push("Ani");

// Hapus berdasarkan index
daftarNama.splice(0, 1);          // Hapus index 0

// Cek apakah ada
daftarNama.includes("Budi");      // true / false

// Loop
daftarNama.forEach(function(nama) {
    console.log(nama);
});

// Jumlah item
daftarNama.length;
```

### Contoh: Simpan & Tampilkan Data ke Tabel
```html
<input type="text" id="inputNama">
<button id="btnTambah">Tambah</button>
<ul id="listNama"></ul>

<script>
    let daftar = [];

    document.getElementById("btnTambah").addEventListener("click", function() {
        const nama = document.getElementById("inputNama").value;
        if (nama === "") return;

        daftar.push(nama);
        tampilkanData();
        document.getElementById("inputNama").value = "";     // Kosongkan input
    });

    function tampilkanData() {
        let html = "";
        daftar.forEach(function(nama, index) {
            html += "<li>" + nama + " <button onclick='hapus(" + index + ")'>Hapus</button></li>";
        });
        document.getElementById("listNama").innerHTML = html;
    }

    function hapus(index) {
        daftar.splice(index, 1);
        tampilkanData();
    }
</script>
```

## Utility
```javascript
setTimeout(function() { ... }, 3000);         // Sekali setelah 3 detik
setInterval(function() { ... }, 1000);        // Berulang tiap 1 detik

localStorage.setItem("nama", "Budi");         // Simpan
localStorage.getItem("nama");                 // Ambil
localStorage.removeItem("nama");              // Hapus

console.log("debug");
alert("Pesan");
confirm("Yakin?");                             // true / false
```
