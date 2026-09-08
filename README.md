# Tugas DDP - Program Rekap Nilai Mahasiswa

Program ini dibuat untuk membantu dosen yaitu pak bruce dalam menginput dan memisahkan nilai mahasiswa yang lulus dan yang harus remedi, serta bisa menghapus nilai jika ada yang salah ketik.

---

## Penjelasan Kode Program

1. **Variabel dan Batas Nilai**
   - Batas nilai lulus ditentukan 65 dan batas maksimal 100.
   - Menggunakan list `nilai_masuk` untuk menampung semua nilai, list `lulus` untuk nilai yang lulus, dan list `remedi` untuk yang remedi.
   - Menggunakan variabel `jumlah_nilai` untuk menghitung berapa banyak nilai yang sudah dimasukkan.

2. **Input dan Pengecekan Nilai**
   - Menggunakan perulangan `while True` agar kita bisa terus memasukkan nilai sampai mengetik `selesai`.
   - Nilai yang diinput harus di antara 0 sampai 100.
   - Nilai 65 ke atas otomatis masuk ke list `lulus`, sedangkan nilai di bawah 65 masuk ke list `remedi`.
   - Saat mengetik `selesai`, program mengecek apakah nilai yang diinput sudah minimal 5 dan harus ada kombinasi nilai yang lulus serta remedi. Jika belum, program akan meminta input nilai lagi.

3. **Menghapus Nilai (Jika Salah Input)**
   - Program akan menampilkan daftar nilai dan menanyakan apakah ada nilai yang mau dihapus.
   - Jika memilih `ya`, kita bisa memasukkan angka yang ingin dibuang dari daftar.
   - Nilai tersebut otomatis terhapus dari list dan jumlah nilai akan berkurang.

4. **Hasil Akhir**
   - Program menampilkan ringkasan akhir: semua nilai yang tersimpan, nilai lulus, dan nilai remedi.

---

## Hasil Output Program

### Screenshot Output

![Screenshot Output](screenshot.png)
