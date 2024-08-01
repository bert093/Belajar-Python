# kosong test
# * 1. Fungsi tanpa pengembalian nilai
def sapa(nama): # dalam contoh ini sapa adalah fungsi dan nama adalah parameter
    print(f"Halo {nama} ! Selamat datang di program saya")

# memanggil fungsi
sapa("Syahril")
sapa("Andi")



# * 2. Fungsi dengan pengembalian nilai
def tambah(a, b):
    hasil = a + b # anggap seperti rumusnya contoh kita ingin menjumlahkan sesuatu.
    return hasil  #  mengembalikan hasil penjumlahan ke tempat fungsi tersebut dipanggil

# memanggil fungsi tambah dan menyimpan hasilnya di variabel hasil hasil
hasil = tambah(5, 7)
print(f"Hasil Penjumlahannya adalah {hasil}")



# * 3. Fungsi dengan beberapa pengembalian nilai
def operasi(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    perkalian = a * b
    pembagian = a / b
    return penjumlahan, pengurangan, perkalian, pembagian 

# Memanggil fungsi 'operasi' dan menyimpan hasilnya di variabel masing-masing
penjumlahan, pengurangan, perkalian, pembagian = operasi(10, 2)
print(f"penjulahan: {penjumlahan}")
print(f"penjulahan: {pengurangan}")
print(f"penjulahan: {perkalian}")
print(f"penjulahan: {pembagian}")