#TUGAS NOMOR 1
kendaraan = ["Avanza", "mobil", "1500cc", "hitam", "4ronda"]
print("list awal: ")
print(kendaraan)

# menambahkan harga dan tipe kendaraan di belakang
kendaraan.append("243 juta")
kendaraan.append("CVT")

# menambahkan merek kendaraan
kendaraan.insert(2, "toyota")

print("/nList kendaraan setelah ditambahkan :")
print(kendaraan)
print()

  
#TUGAS NOMOR 2
print("silakan pilih bangun datar")
print("1. persegi")
print("2. lingkaran")
print("3. segitiga")

pilih_bangun_datar = int(input("pilih bangun datar: "))

match pilih_bangun_datar:
    case 1:
        sisi = float(input("masukkan sisi: "))
        luas = sisi * sisi
        print("luas persegi =", luas)
        
    case 2:
        jari = float(input("masukkan jari jari:"))
        luas = 3.14 * jari ** 2
        print("luas lingkaran=", luas)
        
    case 3:
        alas = float(input("masukkan alas:"))
        tinggi = float(input("masukkan tinggi:"))
        luas = 0.5 * alas * tinggi
        print("luas segitiga=", luas)
        
    case _:
        print("kamu salah pilih")
        