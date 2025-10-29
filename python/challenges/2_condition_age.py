# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
umur = int(input("Masukan Umur Anda : "))

#Validasi umur
if umur < 12:
    kategori = "Anak Anak"
elif umur < 17:
    kategori = "Remaja"
elif umur < 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

# 2. TODO Tentukan kategori berdasarkan usia
print("Katergori : ", kategori)