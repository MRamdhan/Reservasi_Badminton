# 🏸 Sistem Aplikasi Reservasi Lapangan Badminton

## Deskripsi

Sistem Aplikasi Reservasi Lapangan Badminton merupakan aplikasi berbasis web yang dibangun menggunakan bahasa pemrograman **Python** dengan framework **Flask**, database **MySQL**, serta menerapkan konsep **Object-Oriented Programming (OOP)**. Aplikasi ini bertujuan untuk mempermudah proses reservasi lapangan badminton secara digital sehingga pengguna dapat melihat jadwal ketersediaan lapangan, melakukan reservasi, serta meminimalisir terjadinya bentrok jadwal.

Pada aplikasi ini, pengguna dapat melihat informasi lapangan tanpa harus login. Namun, ketika ingin melakukan reservasi, pengguna diwajibkan melakukan login terlebih dahulu. Setiap reservasi yang dilakukan akan berstatus **Pending** dan harus mendapatkan konfirmasi dari administrator. Administrator memiliki hak akses untuk mengelola data lapangan, mengonfirmasi reservasi, membatalkan reservasi, mengubah status permainan, serta melihat riwayat reservasi.

---

## Fitur Aplikasi

### User

- Melihat daftar lapangan
- Melihat detail lapangan
- Melihat timeline ketersediaan lapangan
- Registrasi akun
- Login
- Reservasi berdasarkan tanggal
- Reservasi berdasarkan jam mulai dan jam selesai
- Validasi jadwal bentrok secara otomatis
- Status reservasi (Pending)

### Admin

- Login sebagai admin
- Dashboard reservasi
- Konfirmasi reservasi
- Membatalkan reservasi
- Mengubah status menjadi:
  - Approved
  - Play
  - Finished
- Melihat nomor telepon pelanggan
- CRUD Data Lapangan
- History Reservasi

---

## Teknologi yang Digunakan

- Python 3.x
- Flask
- SQLAlchemy
- MySQL
- HTML
- CSS
- JavaScript

---

## Konsep OOP yang Diimplementasikan

- Class
- Object
- Encapsulation
- Inheritance
- Polymorphism

---

# Database

File database dapat diunduh melalui Google Drive berikut:

**Link Database (.zip)**

👉 **https://drive.google.com/drive/folders/1-vSYekbufk6GrF2pVDehfbQAskrPG4p1?usp=drive_link**

---
# Demo

Video Demo Aplikasi dapat dilihat melalui Link Youtube Berikut:

**Link Youtube**

👉 ****

---

# Cara Menjalankan Aplikasi

## 1. Clone Repository

```bash
git clone https://github.com/MRamdhan/Reservasi_Badminton.git
```

Masuk ke folder project

```bash
cd BadmintonReservation
```

---

## 2. Install Python

Pastikan Python 3 sudah terinstall.

Cek versi Python

```bash
python --version
```

---

## 3. Install Library

Install seluruh dependency

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install PyMySQL
```

atau jika tersedia file requirements.txt

```bash
pip install -r requirements.txt
```

---

## 4. Jalankan XAMPP

Aktifkan:

- Apache
- MySQL

---

## 5. Import Database

1. Download file database melalui Google Drive.
2. Ekstrak file ZIP.
3. Salin folder **badminton_db** ke direktori berikut:

```
xampp/mysql/data/
```

---

## 6. Konfigurasi Database

Pastikan konfigurasi pada file **app.py**

```python
app.config["SQLALCHEMY_DATABASE_URI"] = \
"mysql+pymysql://root:@localhost/badminton_db"
```

Jika password MySQL berbeda, sesuaikan konfigurasi tersebut.

---

## 7. Jalankan Aplikasi

Buka terminal pada folder project kemudian jalankan

```bash
python app.py
```

Apabila berhasil akan muncul

```
Running on http://127.0.0.1:5000
```

---

## 8. Buka Browser

Masukkan alamat berikut

```
http://localhost:5000
```

atau

```
http://127.0.0.1:5000
```

---

# Struktur Project

```
BadmintonReservation
│
├── app.py
├── database.py
├── controllers/
├── models/
├── templates/
├── static/
├── utils/
└── README.md
```
