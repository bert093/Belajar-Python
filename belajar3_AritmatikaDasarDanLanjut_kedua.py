angka = int(input("Masukkan jumlah uang yang ingin ditambahkan: "))
angka_lagi = int(input("Masukkan jumlah uang lagi yang ingin ditambahkan: "))
hasil = angka + angka_lagi

formatted_hasil = f"{hasil:,}".replace(",", ".")
print (f"Hasil yang anda masukkan adalah Rp{formatted_hasil}")

#* print (f"Hasil yang anda masukkan adalah {hasil}") print normal