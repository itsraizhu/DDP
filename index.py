batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []
jumlah_nilai = 0

print("Batas Nilai Lulus :", batas_nilai[0])
print("Nilai Maksimal    :", batas_nilai[1])
print("Ketik 'selesai' jika sudah selesai.")

while True:
    input_user = input("Masukkan nilai: ")
    
    if input_user == "selesai":
        if jumlah_nilai < 5:
            print("Minimal harus memasukkan 5 nilai! (Baru masuk:", jumlah_nilai, ")")
            continue
            
        ada_lulus = False
        ada_remedi = False
        for n in nilai_masuk:
            if n >= batas_nilai[0]:
                ada_lulus = True
            else:
                ada_remedi = True
                
        if ada_lulus == False or ada_remedi == False:
            print("Harus ada minimal satu nilai lulus dan satu nilai remedi!")
            continue
            
        break

    nilai = int(input_user)

    if nilai < 0 or nilai > batas_nilai[1]:
        print("Nilai tidak valid! Masukkan angka antara 0 - 100.")
        continue
        
    nilai_masuk.append(nilai)
    jumlah_nilai += 1

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
        print("Status: Lulus")
    else:
        remedi.append(nilai)
        print("Status: Remedi")

print("DATA NILAI")
print("Semua Nilai :", nilai_masuk)
print("Lulus       :", lulus)
print("Remedi      :", remedi)

pilihan_hapus = input("Ada nilai yang mau dihapus? (ya/tidak): ")

if pilihan_hapus == "ya":
    while True:
        print("Daftar nilai:", nilai_masuk)
        input_hapus = input("Masukkan nilai yang mau dihapus (atau ketik 'selesai'): ")
        
        if input_hapus == "selesai":
            break
            
        nilai_hapus = int(input_hapus)

        if nilai_hapus in nilai_masuk:
            nilai_masuk.remove(nilai_hapus)
            jumlah_nilai -= 1

            if nilai_hapus >= batas_nilai[0]:
                lulus.remove(nilai_hapus)
            else:
                remedi.remove(nilai_hapus)
                
            print("Nilai", nilai_hapus, "berhasil dihapus.")
            
            tanya_lagi = input("Mau hapus nilai lain? (ya/tidak): ")
            if tanya_lagi != "ya":
                break
        else:
            print("Nilai tidak ada di dalam daftar!")

print("1. Semua Nilai :", nilai_masuk)
print("2. Nilai Lulus :", lulus)
print("3. Nilai Remedi:", remedi)
